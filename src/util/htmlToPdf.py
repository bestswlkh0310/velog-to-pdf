import pdfkit

def htmlToPdf(url, outputName):
    options = {
        'margin-top': '0',
        'margin-right': '0',
        'margin-bottom': '0',
        'margin-left': '0',
        'disable-smart-shrinking': True
    }

    print(f'{outputName}.pdf')

    try:
        pdfkit.from_url(url, f'{outputName}.pdf', options=options)
    except Exception as e:
        print(e)