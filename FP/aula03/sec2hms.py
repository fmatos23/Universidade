def sec2hms(segundos):
    s = segundos % 60
    m = segundos // 60 % 60
    h = segundos // 3600
    return h,m,s
