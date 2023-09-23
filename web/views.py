from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,"web/index.html")
def research(request):
    return render(request,"web/research.html")
def project(request):
    return render(request,"web/project.html")
def skill(request):
    return render(request,"web/skill.html")
def course(request):
    return render(request,"web/course.html")
def award(request):
    return render(request,"web/award.html")
def switch(request):
    return render(request,"web/switch.html")

#
# def Audio8D(request):
#     def conv8D(data):
#         m = data.shape
#         if len(m) == 1:
#             data3 = data
#             del data
#             data = np.zeros((m[0], 2), dtype=np.int16)
#             data[:, 0] = data3
#             data[:, 1] = data3
#         m = data.shape
#         data2 = np.zeros(data.shape, dtype=np.int16)
#         n = rate * speed
#
#         for i in range(0, m[0]):
#             if (i % n < n / 2):
#                 data2[i][0] = data[i][0] * (i % (n / 2)) / (n / 2)
#                 data2[i][1] = data[i][1] * ((n - i) % (n / 2)) / (n / 2)
#             else:
#                 data2[i][1] = data[i][1] * (i % (n / 2)) / (n / 2)
#                 data2[i][0] = data[i][0] * ((n - i) % (n / 2)) / (n / 2)
#         return data2
#
#     path = settings.MEDIA_ROOT
#
#     if (os.path.isdir(path)):
#         shutil.rmtree(path)
#
#     context = {}
#
#     if request.method == "POST":
#
#         if len(request.FILES) != 0:
#             uploaded_file = request.FILES["document"]
#             fs = FileSystemStorage()
#
#             spd = str(request.POST["speed"])
#
#             if spd == "x0.25":
#                 speed = 64
#             elif spd == "x0.50":
#                 speed = 32
#             elif spd == "x0.75":
#                 speed = 22
#             elif spd == "x1.00":
#                 speed = 16
#             elif spd == "x1.25":
#                 speed = 14
#             elif spd == "x1.50":
#                 speed = 12
#             elif spd == "x1.75":
#                 speed = 10
#             else:
#                 speed = 8
#
#             name = fs.save(uploaded_file.name, uploaded_file)
#             name2 = name[0:len(name) - 4] + "--8D--" + spd + ".mp3"
#             name2wav = name[0:len(name) - 4] + "--8D--" + spd + ".wav"
#             name3 = name[0:len(name) - 4] + ".wav"
#
#             context['spd'] = spd
#             context['url'] = fs.url(name)
#             context['url_m'] = name.replace(" ", "")
#
#             if name[len(name) - 4:len(name)] == ".mp3" or name[len(name) - 4:len(name)] == ".wav":
#
#                 if name[len(name) - 4:len(name)] == ".mp3":
#
#                     AudioSegment.from_mp3(os.path.join(path, name)).export(os.path.join(path, name3), format="wav")
#
#                 else:
#                     name3 = name
#
#                 rate, data = scipy.io.wavfile.read(os.path.join(path, name3))
#
#                 scipy.io.wavfile.write(os.path.join(path, name2wav), rate, conv8D(data))
#
#                 AudioSegment.from_wav(os.path.join(path, name2wav)).export(os.path.join(path, name2), format="mp3")
#
#                 os.remove(os.path.join(path, name2wav))
#
#                 context['url2'] = fs.url(name2)
#                 context['url2_m'] = name2.replace(" ", "")

    # return render(request, 'app1/for8D/upload.html', context)
