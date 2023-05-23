$ErrorActionPreference = 'Stop'

$url32       = ''
$checksum32  = ''

$packageArgs = @{
  packageName    = $Env:ChocolateyPackageName
  fileType       = 'EXE'
  url            = $url32
  checksum       = $checksum32
  checksumType   = 'sha256'
  silentArgs     = '/S'
  validExitCodes = @(0)
}
Install-ChocolateyPackage @packageArgs
