
''' Want to create your own modules? Ofcoures you do because its great to write
    and use your own code...
    To do this you need to find where all of your python modules are installed.
    I did this by first importing a package I knew I installed properly, such
    as numpy so in my interpreter I typed

    import numpy
    numpy.__file__

    which returned the location of the numpy module which looked like this

    /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages

    once you have this, you can simply create the module you would like, for example
    lets create one called hello.py which contains the following code
    
    def hello():
        print('Hello!')

    Save this file to a known diretory, for this case we will put it on the desktop.

    Then we will move this to the location in which python can find it and import it
    that being the location you installed numpy. To do this, in terminal type

    mv /Users/owenmannion/Desktop/Hello.py /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages

    and that should do it. To test that it is intalled correctly try and import
    and run the funtion.

    import Hello
    Hello.hello()

    which should type out Hello!

    '''
    
