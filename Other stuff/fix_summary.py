import os

import tensorflow as tf
from tensorflow.core.util.event_pb2 import Event


def fix_events(input_path: str, output_path: str):
    # Make a record writer
    with tf.io.TFRecordWriter(output_path) as writer:
        # Iterate event records
        for rec in tf.data.TFRecordDataset([input_path]):
            # Read event
            ev = Event()
            ev.MergeFromString(rec.numpy())
            # Check if it is a summary
            if ev.summary:
                # Iterate summary values
                for v in ev.summary.value:
                    # Check if the tag should be renamed
                    if v.tag == 'train_acc':
                        v.simple_value *= 100
            writer.write(ev.SerializeToString())


if __name__ == '__main__':
    name = 'events.out.tfevents.1647967329.DESKTOP-I1Q6GKF'
    temp_name = 'temp_events'
    fix_events(name, temp_name)
    os.replace(temp_name, name)
