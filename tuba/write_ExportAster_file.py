import psutil
import logging
logging.info(psutil.virtual_memory())
# Code Aster Version
CdAver="v14.4_smeca"
# Memory for Job
JOBmem=3000000
#90% of available meomry in MB
TOTmem=psutil.virtual_memory()[1]/1024/1024*0.9
# Nr. of CPUs for OpenMPI
OpenMPIcpu=psutil.cpu_count()
logging.info("CPU"+str(OpenMPIcpu))
# Nr. of CPUs for MUMPS
MUMPScpu=1

def writeExport(cmd_script,outputFile_ExportAster,
                outputFile_Comm, aster_root,resultfile_aster,current_directory):
    lines=[]

    lines=(
"""P aster_root """+aster_root+"""
P version """+str(CdAver)+"""
P lang en 
P ncpus """+str(OpenMPIcpu)+"""
P mpi_nbcpu """+str(MUMPScpu)+"""
P mpi_nbnoeud 1
A memjeveux """+str(TOTmem)+"""
P mem_aster 100.0 
A tpmax 9000000 
P memjob """+str(JOBmem)+"""
P memory_limit 3000
P actions make_etude 

F mmed """+current_directory+"/"+cmd_script+""".mmed D 20
F comm """+outputFile_Comm+""" D 1 
F resu """+current_directory+"/"+cmd_script+""".resu.txt R 8 
F mess """+current_directory+"/"+cmd_script+""".mess R 6 
F rmed """+resultfile_aster+""" R 80 
""").split("\n") 
    
    try:
       f = open(outputFile_ExportAster, 'w')
       f.write('\n'.join(lines))
       f.close()
    except:
        logging.error("Error while writing the ExportAster-File")        