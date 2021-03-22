from pdf2image import convert_from_path
from pyzbar.pyzbar import decode


_pdf_path = r'.\data\qr_test.pdf'
_removal_list = ['Rect(left=', 'top=', 'width=', 'height=', ')']
_num_page = 1
_output_path = r'convert_pdf'


def converter_pdf(arg_path_pdf, arg_output_path, arg_num_page):
    img = convert_from_path(
        arg_path_pdf,
        dpi=200,
        output_folder=arg_output_path,
        first_page=arg_num_page,
        last_page=arg_num_page,
        fmt="png",
        jpegopt=None,
        thread_count=1,
        userpw=None,
        use_cropbox=True,
        strict=False,
        transparent=False,
        single_file=False,
        output_file=r'convert_file',
        poppler_path=r'C:\Program Files\poppler-0.68.0\bin',
        grayscale=False,
        size=None,
        paths_only=False,
    )
    return img[0]


def qr_load(output_file_path):
    decoded_qr = {}
    img_bars = decode(output_file_path)
    for bar in img_bars:
        decoded_qr[bar.data] = bar.rect
    return decoded_qr


def qr_iterable(def_load):
    new_qr = {}
    for key, value in def_load.items():
        new_values = (str(value))
        for word in _removal_list:
            new_values = new_values.replace(word, '')
        x = new_values.split(', ')
        zzz = integer_list(x)
        new_qr[key] = integer_list(zzz)
    return new_qr


def pythagoras(x_list):
    pif = (x_list[0]**2 + x_list[1]**2)
    return pif


def integer_list(arg_list):
    return [int(i) for i in arg_list]


def output_qr(arg_qr_iterable):
    first_load = -1
    output_data = ''
    for key, values in arg_qr_iterable.items():
        x = pythagoras(values)
        if first_load < x or first_load == -1:
            first_load = x
            output_data = key
    return output_data


def main():
    converter_pdf(_pdf_path, _output_path, _num_page)
    arg_converter = converter_pdf(_pdf_path, _output_path, _num_page)
    qr_load(arg_converter)
    x = qr_load(arg_converter)
    qr_iterable(x)
    ppp = qr_iterable(x)
    return output_qr(ppp)


print(main())
