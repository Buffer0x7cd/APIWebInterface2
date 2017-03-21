from django.conf.urls import url,include
from django.contrib import admin
from AuthPortal.views import signup,login_user

app_name='APIWebInterface'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^check/', include('AuthPortal.urls')),
]

# dded the login patterns

urlpatterns += [
    url(r'^signup/', signup, name="signup"),
    url(r'^login/', login_user, name="login"),
]
