function Show-Tree {
    param (
        [string]$Path = ".",
        [int]$Level = 0,
        [string]$OutputFile = "estrutura_projeto.txt"
    )

    $items = Get-ChildItem -Path $Path | Where-Object { $_.Name -notmatch "venv|__pycache__|trash|.vscode" }

    foreach ($item in $items) {
        # Monta a linha com indentação
        $line = (" " * ($Level * 4) + "|-- " + $item.Name)

        # Exibe no terminal e escreve no arquivo
        Write-Output $line | Tee-Object -FilePath $OutputFile -Append

        if ($item.PSIsContainer) {
            Show-Tree -Path $item.FullName -Level ($Level + 1) -OutputFile $OutputFile
        }
    }
}

# Remove o arquivo anterior para evitar duplicação
Remove-Item "estrutura_projeto.txt" -ErrorAction SilentlyContinue

# Executa a função e gera o arquivo
Show-Tree
