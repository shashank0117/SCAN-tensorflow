import tensorflow as tf


class Encoder(object):
    def __init__(self, cfg):
        self.cfg = cfg

    def __call__(self, input):
        if self.cfg.DAENoiseType == "gaussian":  # additive gaussian noise
            noise = self.cfg.scale * tf.random_normal(shape=input.get_shape())
            input = input + noise
        elif self.cfg.DAENoiseType == "mask":  # masking noise
            input = tf.nn.dropout(input, self.cfg.keep_prob)
        h1 = tf.contrib.layers.conv2d(input, num_outputs=32, kernel_size=4,
                                      strde=2, activation_fn=tf.nn.elu)
        h2 = tf.contrib.layers.conv2d(h1, num_outputs=32, kernel_size=4,
                                      strde=2, activation_fn=tf.nn.elu)
        h3 = tf.contrib.layers.conv2d(h2, num_outputs=64, kernel_size=4,
                                      strde=2, activation_fn=tf.nn.elu)
        h4 = tf.contrib.layers.conv2d(h3, num_outputs=64, kernel_size=4,
                                      strde=2, activation_fn=tf.nn.elu)

        return(h4)


class Decoder(object):
    def __init__(self, cfg):
        self.cfg = cfg

    def __call__(self, input):
        input = tf.contrib.layers.fully_connected(input)
        h1 = tf.contrib.layers.conv2d_transpose(input, num_outputs=64,
                                                kernel_size=4, stride=2,
                                                activation_fn=tf.nn.elu)
        h2 = tf.contrib.layers.conv2d_transpose(h1, num_outputs=64, stride=2,
                                                kernel_size=4,
                                                activation_fn=tf.nn.elu)
        h3 = tf.contrib.layers.conv2d_transpose(h2, num_outputs=32, stride=2,
                                                kernel_size=4,
                                                activation_fn=tf.nn.elu)
        h4 = tf.contrib.layers.conv2d_transpose(h3, num_outputs=32, stride=2,
                                                kernel_size=4,
                                                activation_fn=tf.nn.elu)

        return(h4)


if __name__ == "__main__":
    pass
