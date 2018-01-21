# This file is generated by /Volumes/100GB/conda/conda-bld/scipy_1506097744402/work/setup.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

openblas_lapack_info={}
mkl_info={'libraries': ['mkl_rt', 'pthread'], 'library_dirs': ['/Users/xukaiqiang/anaconda3/lib'], 'define_macros': [('SCIPY_MKL_H', None)], 'include_dirs': ['/Users/xukaiqiang/anaconda3/include']}
lapack_mkl_info={'libraries': ['mkl_rt', 'pthread'], 'library_dirs': ['/Users/xukaiqiang/anaconda3/lib'], 'define_macros': [('SCIPY_MKL_H', None)], 'include_dirs': ['/Users/xukaiqiang/anaconda3/include']}
lapack_opt_info={'libraries': ['mkl_rt', 'pthread'], 'library_dirs': ['/Users/xukaiqiang/anaconda3/lib'], 'define_macros': [('SCIPY_MKL_H', None)], 'include_dirs': ['/Users/xukaiqiang/anaconda3/include']}
blas_mkl_info={'libraries': ['mkl_rt', 'pthread'], 'library_dirs': ['/Users/xukaiqiang/anaconda3/lib'], 'define_macros': [('SCIPY_MKL_H', None)], 'include_dirs': ['/Users/xukaiqiang/anaconda3/include']}
blas_opt_info={'libraries': ['mkl_rt', 'pthread'], 'library_dirs': ['/Users/xukaiqiang/anaconda3/lib'], 'define_macros': [('SCIPY_MKL_H', None)], 'include_dirs': ['/Users/xukaiqiang/anaconda3/include']}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    