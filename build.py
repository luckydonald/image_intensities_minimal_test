import platform
from cffi import FFI
from pathlib import Path

image_intensities_root_path = Path(__file__).parent
image_intensities_sources_path = image_intensities_root_path / "sources"

image_intensities_definitions = """
    extern struct intensity_data {
        double nw;
        double ne;
        double sw;
        double se;
        int error;
    } intensity_data;

    struct intensity_data jpeg_intensities(const char *file_name);
    struct intensity_data png_intensities(const char *file_name);
"""


def prepare_variant():
    header_path = (image_intensities_sources_path / "definitions.h").resolve()
    extra_kwargs = {}

    ffi = FFI()
    ffi.cdef("""
        typedef struct intensity_data {
            double nw;
            double ne;
            double sw;
            double se;
            int error;
        } intensity_data;

        struct intensity_data jpeg_intensities(const char *file_name);
        struct intensity_data png_intensities(const char *file_name);
    """)

    sources = [
        "sources/intensities.c",
        "sources/jpeg.c",
        "sources/png.c",

        "sources/turbojpeg/jcparam.c",
        "sources/turbojpeg/jdcolext.c",
        "sources/turbojpeg/jdicc.c",
        "sources/turbojpeg/jcapistd.c",
        "sources/turbojpeg/jdarith.c",
        "sources/turbojpeg/jctrans.c",
        "sources/turbojpeg/jcdctmgr.c",
        "sources/turbojpeg/jdhuff.c",
        "sources/turbojpeg/jfdctflt.c",
        "sources/turbojpeg/jcphuff.c",
        "sources/turbojpeg/jerror.c",
        "sources/turbojpeg/jdatasrc.c",
        "sources/turbojpeg/jdsample.c",
        "sources/turbojpeg/jdinput.c",
        "sources/turbojpeg/jdtrans.c",
        "sources/turbojpeg/jdmainct.c",
        "sources/turbojpeg/jcmainct.c",
        "sources/turbojpeg/jcapimin.c",
        "sources/turbojpeg/jccoefct.c",
        "sources/turbojpeg/jcicc.c",
        "sources/turbojpeg/jccolext.c",
        "sources/turbojpeg/jdmrgext.c",
        "sources/turbojpeg/jddctmgr.c",
        "sources/turbojpeg/jdapimin.c",
        "sources/turbojpeg/jcmaster.c",
        "sources/turbojpeg/jfdctfst.c",
        "sources/turbojpeg/jdatadst.c",
        "sources/turbojpeg/jdcolor.c",
        "sources/turbojpeg/jcinit.c",
        "sources/turbojpeg/jcomapi.c",
        "sources/turbojpeg/jcarith.c",
        "sources/turbojpeg/jdapistd.c",
        "sources/turbojpeg/jchuff.c",
        "sources/turbojpeg/jdmaster.c",
        "sources/turbojpeg/jdatadst-tj.c",
        "sources/turbojpeg/jdcoefct.c",
        "sources/turbojpeg/jcsample.c",
        "sources/turbojpeg/jdmrg565.c",
        "sources/turbojpeg/jdcol565.c",
        "sources/turbojpeg/jdmerge.c",
        "sources/turbojpeg/jccolor.c",
        "sources/turbojpeg/jdphuff.c",
        "sources/turbojpeg/jdmarker.c",
        "sources/turbojpeg/jaricom.c",
        "sources/turbojpeg/jcmarker.c",
        "sources/turbojpeg/jcprepct.c",
        "sources/turbojpeg/jfdctint.c",
        "sources/turbojpeg/jdatasrc-tj.c",
        "sources/turbojpeg/jdpostct.c",
        "sources/turbojpeg/jidctflt.c",
        "sources/turbojpeg/jidctfst.c",
        "sources/turbojpeg/jidctint.c",
        "sources/turbojpeg/jidctred.c",
        "sources/turbojpeg/jmemmgr.c",
        "sources/turbojpeg/jmemnobs.c",
        "sources/turbojpeg/jquant1.c",
        "sources/turbojpeg/jquant2.c",
        "sources/turbojpeg/jsimd_none.c",
        "sources/turbojpeg/jstdhuff.c",
        "sources/turbojpeg/jutils.c",
        "sources/turbojpeg/rdbmp.c",
        "sources/turbojpeg/rdppm.c",
        "sources/turbojpeg/transupp.c",
        "sources/turbojpeg/turbojpeg.c",
        "sources/turbojpeg/wrbmp.c",
        "sources/turbojpeg/wrppm.c",
    ]

    include_dirs = [  # -I
        'sources/',
        'sources/turbojpeg/',
    ]
    libraries = [  # -L
        'sources/jpeg',
        'sources/png',
    ]

    if "Windows" in platform.system():
        extra_kwargs["extra_link_args"] = ["/NODEFAULTLIB:MSVCRTD"]
        extra_kwargs["libraries"] = ["advapi32"]

    ffi.set_source(
        'images_intensities._intensities',
        f'#include "{ str(header_path) }"',
        sources=sources,
        include_dirs=include_dirs,  # -I
        libraries=libraries,  # -L
        **extra_kwargs,
    )

    return ffi
# end def


intensities_ffi = prepare_variant()

if __name__ == "__main__":
    intensities_ffi.compile(verbose=True)
