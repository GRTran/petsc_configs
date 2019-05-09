#!/home/gre18/anaconda2/bin/python
if __name__ == '__main__':
  import sys
  import os
  sys.path.insert(0, os.path.abspath('config'))
  import configure
  configure_options = [
    '--prefix=/home/gre18/Documents/Codes/Fortran-Codes/PETSc/linux_optD',
    '--with-cc=mpicc',
    '--with-cxx=mpicxx',
    '--with-debugging=1',
    '--with-fc=mpif90',
    '--with-mpi=1',
    '--with-x=1',
    'FOPTFLAGS=-g -O2',
    'PETSC_ARCH=linux_optD',
  ]
  configure.petsc_configure(configure_options)