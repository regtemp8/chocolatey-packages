$ErrorActionPreference = 'Stop'

$url64       = ''
$checksum64  = ''

$toolsPath = Split-Path $MyInvocation.MyCommand.Definition

$packageArgs = @{
  packageName    = $env:ChocolateyPackageName
  url64Bit       = $url64
  checksum64     = $checksum64
  checksumType64 = 'sha256'
  unzipLocation  = $toolsPath
}

Install-ChocolateyZipPackage @packageArgs

if (Test-Path $toolsPath/install.ps1) { . $toolsPath/install.ps1 }
