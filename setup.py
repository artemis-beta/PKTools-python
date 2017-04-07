from setuptools import setup

setup(name                =  'pktools'                                             ,
      version             =  '0.1.0'                                               ,
      description         =  'Physics Kit Tools for Python'                        ,
      url                 =  'http://github.com/artemis-beta/pktools-python'       ,
      author              =  'Kristian Zarebski'                                   ,
      author_email        =  'krizar312@yahoo.co.uk'                               ,
      license             =  'MIT'                                                 ,
      packages            =  ['pktools']                                           ,
      zip_safe            =  False                                                 ,
      tests_require       =  ['pytest']                                            ,
      setup_requires      =  ['pytest-runner']                                     ,
     )
