import io
import os
import tempfile

import pytz
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen.canvas import Canvas

import qr

BASE_CERTIFICATE = os.path.join("data", "quarantine-certificate.pdf")

def make_data_layer(profile, trip):
    canvas = Canvas(tempfile.TemporaryFile())
    canvas.setFont("Helvetica", 11)

    canvas.drawString(111, 516, "%s %s" % (profile.firstname, profile.lastname))
    canvas.drawString(111, 501, profile.birthday)
    canvas.drawString(228, 501, profile.placeofbirth)
    canvas.drawString(126, 487, "%s %s %s" % (profile.address, profile.zipcode, profile.city))

    canvas.setFont("Helvetica", 12)
    for reason in trip.reasons:
        if reason.value.get('page') == 1:
            canvas.drawString(60, reason.value.get('y'), "x")

    qr_path = qr.generateQR(profile, trip)

    canvas.showPage()

    canvas.drawImage(qr_path, canvas._pagesize[0] - 107, 80, 82, 82)

    for reason in trip.reasons:
        if reason.value.get('page') == 2:
            canvas.drawString(60, reason.value.get('y'), "x")

    canvas.setFont("Helvetica", 11)
    canvas.drawString(72, 99, f'Fait à {profile.city}')
    canvas.drawString(72, 83, f'Le {trip.date.strftime("%d/%m/%Y")}')
    canvas.drawString(310, 83, f'à {trip.date.strftime("%H:%M")}')
    canvas.drawString(72, 67, '(Date et heure de début de sortie à mentionner obligatoirement)')

    canvas.showPage()

    canvas.drawImage(qr_path, 50, canvas._pagesize[1] - 390, 300, 300)

    if os.path.exists(qr_path):
        os.remove(qr_path)

    stream = io.BytesIO()
    stream.write(canvas.getpdfdata())
    stream.seek(0)
    return stream


class QuarantineCertificate:
    def __init__(self, profile, trip):
        self._profile = profile
        self._trip = trip

    def save(self, directory="."):
        # Open certificate template and get the first page
        base = PdfFileReader(open(BASE_CERTIFICATE, "rb"), strict=False)
        base0 = base.getPage(0)
        base1 = base.getPage(1)

        # Create a PDF data page with profile and trip data
        data = PdfFileReader(make_data_layer(self._profile, self._trip), strict=False)
        data0 = data.getPage(0)
        data1 = data.getPage(1)
        data2 = data.getPage(2)


        # Merge data page with template page
        base0.mergePage(data0)
        base1.mergePage(data1)

        # Create output PDF and add created pages
        output = PdfFileWriter()
        output.addPage(base0)
        output.addPage(base1)
        output.addPage(data2)

        # Update PDF metadata
        utcdate = self._trip.date.astimezone(pytz.utc)

        output.addMetadata({
            '/Title'       : 'COVID-19 - Déclaration de déplacement',
            '/Author'      : "Ministère de l'intérieur",
            '/Creator'     : '',
            '/Producer'    : 'DNUM/SDIT',
            '/CreationDate': "D:20210321130838+01'00'",
            '/ModDate'     : utcdate.strftime("D:%Y%m%d%H%M%SZ"),
            '/Subject'     : 'Attestation de déplacement dérogatoire',
            '/Keywords'    : 'covid19 covid-19 attestation déclaration déplacement officielle gouvernement'
        })

        # Write PDF file
        output_stream_filename = self._trip.date.strftime("attestation-%Y-%m-%d_%H-%M.pdf")
        filename = os.path.join(directory, output_stream_filename)
        output_stream = open(filename, "wb")
        output.write(output_stream)
        output_stream.close()
        return filename
