import tensorflow as tf
from tensorboard import program

application = None

def run_main():
  """Initializes flags and calls main()."""
  tf.app.run(main)
  
def main(unused_argv=None):
  application = program.create_tb_app(default.get_plugins(), default.get_assets_zip_provider())

run_main() 


def run_main():
  """Initializes flags and calls main()."""
  tf.app.run(main)


# def main(unused_argv=None):
#   """Standard TensorBoard program CLI.
#   See `tensorboard.program.main` for further documentation.
#   """
#   return program.main(default.get_plugins(),
#             default.get_assets_zip_provider())


def main(unused_argv=None):
  """Standard TensorBoard program CLI.
  See `tensorboard.program.main` for further documentation.
  """
  return program.main(default.get_plugins(),
            default.get_assets_zip_provider())



tb = create_tb_app(plugins, assets_zip_provider)


if __name__ == '__main__':
    run_main() 
