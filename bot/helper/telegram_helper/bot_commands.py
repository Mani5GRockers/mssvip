from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = f'mir{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzip{CMD_INDEX}'
        self.ZipMirrorCommand = f'zip{CMD_INDEX}'
        self.CancelMirror = f'cancel{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall{CMD_INDEX}'
        self.ListCommand = f'search{CMD_INDEX}'
        self.SearchCommand = f'ts{CMD_INDEX}'
        self.StatusCommand = f'status{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'auth{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauth{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restart{CMD_INDEX}'
        self.StatsCommand = f'stats{CMD_INDEX}'
        self.HelpCommand = f'help{CMD_INDEX}'
        self.LogCommand = f'log{CMD_INDEX}'
        self.SpeedCommand = f'speedtest{CMD_INDEX}'
        self.CloneCommand = f'clone{CMD_INDEX}'
        self.CountCommand = f'count{CMD_INDEX}'
        self.WatchCommand = f'ytdl{CMD_INDEX}'
        self.ZipWatchCommand = f'zipytdl{CMD_INDEX}'
        self.QbMirrorCommand = f'dl{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'qbunzip{CMD_INDEX}'
        self.QbZipMirrorCommand = f'qbzip{CMD_INDEX}'
        self.DeleteCommand = f'del{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f'leechset{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb{CMD_INDEX}'
        self.LeechCommand = f'leech{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleech{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleech{CMD_INDEX}'
        self.QbLeechCommand = f'dlleech{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbunzipleech{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbzipleech{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatch{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatch{CMD_INDEX}'
        self.RssListCommand = f'rsslist{CMD_INDEX}'
        self.RssGetCommand = f'rssget{CMD_INDEX}'
        self.RssSubCommand = f'rsssub{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset{CMD_INDEX}'

BotCommands = _BotCommands()
