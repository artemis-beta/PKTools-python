from setuptools import setup

setup( name             =       'pktools'                                        ,
       version          =       'v2.0.2'                                         ,
       description      =       'Physics Kit Module'                             ,
       url              =       'https://github.com/artemis-beta/PKTools-python' ,
       author           =       'Kristian Zarebski'                              ,
       author_email     =       'krizar312@yahoo.co.uk'                          ,
       license          =       'MIT'                                            ,
       packages         =       ['pktools']                                      ,
       zip_safe         =       False                                            ,
       install_requires =       ['pint', 'numpy', 'matplotlib']
     )
