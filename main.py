"""The main entry point."""

if __name__ == '__main__':
 import logging
 from default_argparse import parser
 args = parser.parse_args()
 logging.basicConfig(stream = args.log_file, level = args.log_level)
 from version import name, version
 logging.info('Starting %s version %s.', name, version)
 from pyglet import app
 from ui import window
 logging.info('Main window: %s.', window)
 app.run()
 logging.info('Goodbye.')
 
