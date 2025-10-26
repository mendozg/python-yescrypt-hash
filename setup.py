from distutils.core import setup, Extension

yescrypt_hash_module = Extension('yescrypt_hash',
                                 sources = ['yescryptmodule.c',
                                            'yescrypthash.c'],
                               include_dirs=['.', './yescrypt'])

setup (name = 'yescrypt_hash',
       version = '0.5',
       description = 'Binding for Yescrypt proof of work hashing.',
       ext_modules = [yescrypt_hash_module])
