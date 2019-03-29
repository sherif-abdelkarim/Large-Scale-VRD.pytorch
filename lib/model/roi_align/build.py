from __future__ import print_function
import os
import torch
from torch.utils.ffi import create_extension

# sources = ['src/roi_align.c']
# headers = ['src/roi_align.h']
sources = []
headers = []
defines = []
with_cuda = False

if torch.cuda.is_available():
    print('Including CUDA code.')
    sources += ['src/roi_align_cuda.c']
    headers += ['src/roi_align_cuda.h']
    # # By Ji on 08/20/2018
    # sources += ['src/roi_align_rel_cuda.c']
    # headers += ['src/roi_align_rel_cuda.h']
    defines += [('WITH_CUDA', None)]
    with_cuda = True

this_file = os.path.dirname(os.path.realpath(__file__))
print(this_file)
extra_objects = ['src/roi_align_kernel.cu.o']
# # By Ji on 08/20/2018
# extra_objects += ['src/roi_align_rel_kernel.cu.o']
extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

ffi = create_extension(
    '_ext.roi_align',
    headers=headers,
    sources=sources,
    define_macros=defines,
    relative_to=__file__,
    with_cuda=with_cuda,
    extra_objects=extra_objects
)

if __name__ == '__main__':
    ffi.build()
