from django.shortcuts import render
from .models import *
from django.db.models import Sum,Avg,Max,Min,Count,F,Q
from django.http import JsonResponse,HttpResponse

def usergeneratedcontent(request):
    studio_id=request.POST.get('studio_id')
    print(studio_id)

    obj=SdkUsers.objects.raw("select u.id,u.email,u.display_name as name,\
         count(ms.id), ms.id as video_id from sdk_users u, movie_streams\
          ms where u.id = ms.sdk_user_id and u.studio_id=2848 group by ms.id")

    # views=VideoLogs.objects.raw("select count(*) AS total_views,movie_streams.id,video_logs.id,user.id from video_logs\
    #         INNER JOIN  movie_streams on movie_streams.id=video_logs.video_id\
    #         INNER JOIN user ON user.studio_id=movie_streams.studio_id where user.studio_id=2848 GROUP BY video_logs.video_id")

    lst=[]
    dict={}
    j=0
    for i in obj:
        # dict={"email":i.email,"display_name":i.display_name,"no_of_uploads":i.no_of_uploads,"total_comments":i.no_of_comments}
        dict={"email":i.email,"display_name":i.display_name}
        lst.append(dict)
        video_id=i.video_id
        print(video_id)
        j+=1

        obj2=VideoLogs.objects.filter(video_id=video_id).values('video_id').annotate(view_count=Count(id))
        print(list(obj2))
    print(j)
    return JsonResponse(lst,safe=False)


def ajax(request):
    fromdate = request.POST.get('from');
    to=request.POST.get('to');
    fix=request.POST.get('fix')

    if fix is not None:
        format_f=fromdate.split("/")
        format_t=to.split("/")
        fromdate="{}-{}-{}".format(format_f[2],format_f[0],format_f[1])
        to="{}-{}-{}".format(format_t[2],format_t[0],format_t[1])

    obj=Films.objects.filter(last_updated_date__range=[fromdate, to]).all()
    for i in obj:print(i.name)
    print(fromdate,to)
    context = {
        "from":fromdate,
        "to":to,
        "records":obj,
    }

    return render(request,'ajax.html',context)
