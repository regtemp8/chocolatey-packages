import-module chocolatey-au

$releases = 'https://github.com/keepassxreboot/keepassxc/releases'

function global:au_SearchReplace {
    @{
        'tools\chocolateyInstall.ps1' = @{
            "(^[$]url64\s*=\s*)('.*')"      = "`$1'$($Latest.URL64)'"
            "(^[$]checksum64\s*=\s*)('.*')" = "`$1'$($Latest.Checksum64)'"
        }
     }
}

function global:au_GetLatest {
    $download_page = Invoke-WebRequest -Uri $releases -UseBasicParsing

    $re  = "KeePassXC-.+-Win64-LegacyWindows.msi"

    $url = $download_page.links | Where-Object href -match $re | Select-Object -First 1 -expand href

    $version = $url -split '/' | Select-Object -Last 1 -Skip 1
    $url64 = 'https://github.com' + $url

    $Latest = @{ URL64 = $url64; Version = $version }
    return $Latest
}

update -ChecksumFor 64
