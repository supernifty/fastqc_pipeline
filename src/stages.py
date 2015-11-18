'''
Individual stages of the pipeline implemented as functions from
input files to output files.

The run_stage function knows everything about submitting jobs and, given
the state parameter, has full access to the state of the pipeline, such
as config, options, DRMAA and the logger.
'''

from utils import safe_make_dir
from runner import run_stage
import os


class Stages(object):
    def __init__(self, state):
        self.state = state

    def get_stage_options(self, stage, *options):
        return self.state.config.get_stage_options(stage, *options)

    def get_options(self, *options):
        return self.state.config.get_options(*options)

    def original_files(self, output):
        '''Original files'''
        pass


    def stage1(self, input, output):
        '''stage 1'''
        command = "./stage1.sh {input} {output}".format(input=input, output=output)
        run_stage(self.state, 'stage1', command)


    def stage2(self, input, output):
        '''stage 2'''
        command = "./stage2.sh {input} {output}".format(input=input, output=output)
        run_stage(self.state, 'stage2', command)


    def stage3(self, input, output):
        '''stage 3'''
        command = "./stage3.sh {input} {output}".format(input=input, output=output)
        run_stage(self.state, 'stage3', command)


    def stage4(self, input, output):
        '''stage 4'''
        command = "./stage4.sh {input} {output}".format(input=input, output=output)
        run_stage(self.state, 'stage4', command)


    def stage5(self, input, output):
        '''stage 5'''
        command = "./stage5.sh {input} {output}".format(input=input, output=output)
        run_stage(self.state, 'stage5', command)
