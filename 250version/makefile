PRES_DIR = .
WORK_DIR = ./console
DIRG = ${PRES_DIR}/general
DIRR = ${PRES_DIR}/randomc
DIRS = ${PRES_DIR}/special
EXE  = ${WORK_DIR}/NORGsolver
VPATH = ${DIRG}:${DIRR}:${DIRS}

CC       = mpiicpc
CPPFLAGS = -std=c++17 -mkl -O3
CFLAGS   =
CXXFLAGS = $(CFLAGS)
COMPILE  = $(CC) $(CPPFLAGS) $(CXXFLAGS) -c

SRCS := $(wildcard ${DIRG}/*.o) $(wildcard ${DIRR}/*.o) $(wildcard ${DIRS}/*.o)

default: qsub

qsub: ${EXE}
	@echo '______________________________________________________________ qsub ______________________________________________________________'
	@echo ''
	@qsub ${WORK_DIR}/qsub.DPC++CPU.mpi.txt > ${WORK_DIR}/jmwang.job.txt
	@chmod +x ${WORK_DIR}/job.process.DPC++CPU.txt
	@${WORK_DIR}/job.process.DPC++CPU.txt
	@rm -rf ${WORK_DIR}/jmwang.job.txt
	@echo '__________________________________________________________________________________________________________________________________'
	@echo ''

${EXE}:
	@echo '______________________________________________________________ link ______________________________________________________________'
	@echo ''
	$(CC) $(CPPFLAGS) $(CXXFLAGS) -o ${EXE} $(SRCS) $(LIBS)

manpower: ${EXE}
	@echo '_______________________________________ Now you can test by: mpirun -n 24 ./console/NORGsolver____________________________________'

start:
	@echo '______________________________________________________________ start ______________________________________________________________'
	@echo ''

explain:
	@echo '______________________________________________________________ explain ______________________________________________________________'
	@echo ''
	@echo "the following information represents your prgram"
	@echo "final EXE name: $(EXE)"
	@echo "source files: $(SRCS)"
	@echo "object files: $(OBJS)"
	@echo "dependency files: $(DEPS)"

compile:
	@echo '______________________________________________________________ compile ______________________________________________________________'
	@echo ''

%.d:%.cpp
	$(CC) -MM $(CPPFLAGS) $< > $@
	$(CC) -MM $(CPPFLAGS) $< | sed s/\\.o/\\.d/   >> $@

%.o:%.cpp
	$(COMPILE) -o $@ $<

clear:
	-rm -rf bi/*
	-rm -rf io/*.txt
	-rm -rf jmwang.*
	-rm -rf console/NORGsolver

depend:$(DEPS)
	@echo "dependencies are now up-to-date."

-include $(DEPS)
