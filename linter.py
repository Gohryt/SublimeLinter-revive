from SublimeLinter.lint import util, Linter, WARNING


class Revive(Linter):
    cmd = 'revive'
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    tempfile_suffix = 'go'
    error_stream = util.STREAM_STDOUT
    default_type = WARNING
    defaults = {
        'selector': 'source.go'
    }
