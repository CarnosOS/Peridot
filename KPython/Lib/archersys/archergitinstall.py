import os,argparse

class ArcherGitInstall(argparse.Action):
      def __call__(self, parser, namespace, values, option_string=None):
             args = parser.parse_args()
             os.system("gitbin\Git1.9.4\cmd\git clone https://github.com/ArcherSys/" + args.package)