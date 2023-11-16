from django.shortcuts import render

# Create your views here.
# def data_count(request):
#     return render(request, 'count.html')

# def data_result(request):
#     text = request.POST['text']
#     total_len = len(text)
#     no_blank_len = len(text.replace(' ', ''))
#     word_num = text.count(' ')+1
#     return render(request, 'result.html', {'text': text, 'total_len': total_len, 'no_blank_len': no_blank_len, 'word_num': word_num})

def data_main(request):
    return render(request, 'data_main.html')