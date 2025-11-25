AUTOMAKE_OPTIONS = foreign
ACLOCAL_AMFLAGS = -I m4
lib_LTLIBRARIES = libyescrypthash.la
libyescrypthash_la_LDFLAGS = -no-undefined
libyescrypthash_la_SOURCES = \
	yescrypthash.c yescrypthash.h \
  yescrypt/sha256.h yescrypt/sha256_c.h \
  yescrypt/sysendian.h \
  yescrypt/yescrypt-best_c.h yescrypt/yescrypt-platform_c.h \
  yescrypt/yescrypt-opt_c.h yescrypt-simd_c.h
