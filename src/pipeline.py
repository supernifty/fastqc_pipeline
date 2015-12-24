'''
Build the pipeline workflow by plumbing the stages together.
'''

from ruffus import Pipeline, suffix, formatter, add_inputs, output_from
from stages import Stages

def make_pipeline(state):
    '''Build the pipeline by constructing stages and connecting them together'''
    # Build an empty pipeline
    pipeline = Pipeline(name='test_pipeline')
    # Get a list of paths to all the FASTQ files
    input_files = state.config.get_option('files')
    # Stages are dependent on the state
    stages = Stages(state)

    # The original files
    # This is a dummy stage. It is useful because it makes a node in the
    # pipeline graph, and gives the pipeline an obvious starting point.
    pipeline.originate(
        task_func=stages.original_files,
        name='original_files',
        output=input_files)

    pipeline.transform(
        task_func=stages.stage1,
        name='stage1',
        input=output_from('original_files'),
        filter=suffix('.0'),
        output='.1')

    pipeline.transform(
        task_func=stages.stage2,
        name='stage2',
        input=output_from('stage1'),
        filter=suffix('.1'),
        output='.2')

    pipeline.transform(
        task_func=stages.stage3,
        name='stage3',
        input=output_from('stage2'),
        filter=suffix('.2'),
        output='.3')

    pipeline.transform(
        task_func=stages.stage4,
        name='stage4',
        input=output_from('stage3'),
        filter=suffix('.3'),
        output='.4')

    pipeline.transform(
        task_func=stages.stage5,
        name='stage5',
        input=output_from('stage4'),
        filter=suffix('.4'),
        output='.5')

    return pipeline
