#Learning Python Day17

#Virtual Enviornment
'''
For example, we normally, atleast until now, we've been using our system's
python, but when you use a virtual env. it creates a copy of the original
python that is on your system, this way you will have a clean python that
won't be connected to your system, meaning you won't be able to use your
previously installed hundreds of modules and other packages that you'll
have on your system in the future. It is like, the system is the continents
or say mainland, but you don't want to see the stuff you have on your mainland,
so you move to an island, with nothing there. Now, let's see how to create a
virtual env. There won't be any need of using any fns and else so, it will be
all text.

- In a folder. Open the terminal there.
> pip install virtualenv
- Virtualenv is a package, after installing it.
> virtualenv folder_name
- f_n will be short for folder_name from now on
> .\f_n\bin\acivate
- After that, you'll see your (f_n) before your username in terminal
showing you are inside the virtual env.
> deactivate
- This is to exit the virtual env.


Now, if you worked on a project inside a virtualenv and want to share it to a friend,
so you give him the code, but what if the versions of modules you used are different
from the ones your friend uses, since with time modules get upgraded and some fns get
unusable and may cause errors. This is also a reason why virtualenvs are used. Here,
you can send the a requirments list containing the names + the versions of the modules
you used, and with that file your friend can install all those packages and of the same
versions as you. This is also true that you could have also just made a file yourself
but as you will grow, the projects will become bigger than you may think, and writing all
names + versions of all those modules will become a pain in the neck.

- inside the virtualenv
> pip freeze > requirments_whatever_you_want.txt
- Now this file will be made and you can install all packages this way.
> pip install -r ./requirments_whatever_you_want.txt

If pip freeze is used outside the virtualenv. the file will contain the list of all the packages
on the main system not the virtualenv. and the same thing will happen for the pip install, meaning
they will be installed on the mains system.


Also, if you want your virtualenv. to have all the packages installed on the main system, use this.

> virtualenv --system-site-packages f_n
- This will be done while creating that virtaulenv.


Note- If you yourself want to download a specific version of a packages, then, just
add ==version_nameornumber, for example, sklearn==1.9.0
'''