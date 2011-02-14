## Bitlespeak static defines
## Matt Arnold 6/1/10
## Copyright (c) Matt Arnold
## Some rights reserved
## BitleSpeak is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## BitleSpeak is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with BitleSpeak.  If not, see <http://www.gnu.org/licenses/>.

import sys

## These settings are for the ssip driver
## will be moved as soon as i figure out where to put em
## so as not to break anything
LINE_ENDING = '\r\n'
BUFFSIZE = 2048 ## expecting 2^10 bytes lets double that
OK_STATE = '2' ## see ssip docs]
CLIENT_NAME = ":bittlespeak:shandler"

DEBUG = 1
## needed by plugin loader
BASE_PATH = '.'
DATA_DIR = BASE_PATH + '/data'
SITE_CONFIG_DIR = '/etc'
SITE_DATA_DIR = sys.prefix + '/share/bitlespeak'

## GTK author metadata

APP_NAME = 'LitleFrog Reader'
APP_VER = '0.4.0-prealpha'
APP_AUTHORS = ["Matt Arnold"]
APP_COPY ='GPLv3'
APP_DESC = 'A little text to speech toolbar'

## UI stuff
PREF_MSG = "Plese edit bitle.cf for application settings"
ICON_FILE_PATH = '/bitlespeak.xpm'
READ_MSG = "Reading..."
NREAD_MSG = "Not Reading"
PREADING_MSG = "Paused..."

## Microsoft Enums Move to win32.enums after release

#SpeechRunState
MS_SRS_DONE = 1
MS_SRS_SPEAKING = 2

# SpeechVoiceSpeakFlags
#'SpVoice Flags
SVSFDefault = 0
SVSFlagsAsync = 1
SVSFPurgeBeforeSpeak = 2
SVSFIsFilename = 4
SVSFIsXML = 8
SVSFIsNotXML = 16
SVSFPersistXML = 32
#   'Normalizer Flags
SVSFNLPSpeakPunc = 64
#    'Masks
SVSFNLPMask = 64
#SVSFParseMask = 
SVSFVoiceMask = 127
SVSFUnusedFlags = -128
#End Enum

# SAPI Constants
SP_DEF_SETTING = 1024 # I need a large number keep above 1000 to be safe
## Private settings for setuptools

_ST_EMAIL = "mattarnold5@gmail.com"
_ST_AUTHOR = "Matt Arnold"
