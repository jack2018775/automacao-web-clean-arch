<#
    Script: create_template.ps1
    Descrição: Cria a estrutura de pastas e arquivos para um projeto Clean Architecture e DDD com duas opções:
    1. Organização por feature
    2. Sem organização por feature
    Parâmetros:
    -Language: Linguagem a ser utilizada (opções: "Python", "Java", "Php") - obrigatorio.
    -TemplateType: Tipo de template a ser utilizado (opções: "Feature", "Basic") - obrigatorio.
    -FeatureName: Nome da feature de demonstração a ser criada (padrão: "feature_demo") - opcional.

    Exemplo de uso:

#>

param (
    [Parameter(Mandatory=$true)]
    [ValidateSet("Python", "Java", "Php")]
    [string]$Language,

    [Parameter(Mandatory=$true)]
    [ValidateSet("Feature", "Basic")]
    [string]$TemplateType,

    [string]$FeatureName = "feature_demo"
)

function New-Structure {
    param (
        [string[]]$structure
    )
    foreach ($path in $structure) {
        if ([string]::IsNullOrWhiteSpace($path)) {
            Write-Warning "Caminho invpalido: $path"
            continue
        }

        $dir = Split-Path $path
        # if (-not $dir) {
        #     Write-Warning "Não foi possivel extrair o diretório: [$path]"
        #     continue
        # }
        if (!(Test-Path $dir)){
            New-Item -ItemType Directory -Force -Path $dir | Out-Null
        }
        if (!(Test-Path $path)) {
            New-Item -ItemType File -Force -Path $path | Out-Null
        }
    }
}
# Estrutura do projeto por linguagem
$baseStructures = @{
    Python = @{
        Common = @(
            # .vscode
            ".vscode/settings.json",
            ".vscode/launch.json",            

            # Core
            # aqui ficará tudo que é comum a todos os módulos
            "core/__init__.py",
            "core/errors/__init__.py",
            "core/errors/failures.py", 
            "core/errors/exceptions.py",
            "core/utils/__init__.py",
            "core/utils/constants.py",
            "core/utils/helpers.py",
            "core/utils/logging.py",

            # Src
            "src/__init__.py",
            # Configuração
            "config/__init__.py",
            "config/settings.py",


            # Root
            "requirements.txt",
            "README.md",
            ".gitignore",
            ".env",
            "setup.py"
        )
        Basic = @(
            # Domain
            "src/domain/__init__.py",
            "src/domain/entities/__init__.py",
            "src/domain/usecases/__init__.py",
            "src/domain/repositories/__init__.py",

            # Infrastructure
            "src/infrastructure/__init__.py",
            "src/infrastructure/models/__init__.py",
            "src/infrastructure/repositories/__init__.py",
            "src/infrastructure/services/__init__.py",
            
            # Presentation
            "src/presentation/__init__.py",
            "src/presentation/api/__init__.py",
            "src/presentation/web/__init__.py",
            "src/presentation/web/templates/base.html",
            "src/presentation/web/static/css/style.css",
            "src/presentation/web/static/js/main.js",

            "src/presentation/cli/__init__.py",
            "src/presentation/desktop/__init__.py"
        )
        Feature = @(
            # Domain
            "src/$FeatureName/domain/__init__.py",
            "src/$FeatureName/domain/entities/__init__.py",
            "src/$FeatureName/domain/usecases/__init__.py",
            # aqui ficará as interfaces de repositórios de domínio
            # que serão implementadas em infraestrutura
            "src/$FeatureName/domain/repositories/__init__.py",

            # Feature Module
            "src/$FeatureName/__init__.py",
            "src/$FeatureName/infrastructure/__init__.py",
            # aqui ficará as models(DTOs)
            "src/$FeatureName/infrastructure/models/__init__.py",
            # aqui ficará as implementações de repositórios
            "src/$FeatureName/infrastructure/repositories/__init__.py",
            "src/$FeatureName/infrastructure/services/__init__.py",
            
            # Presentation
            # aqui ficará as interfaces de apresentação
            "src/$FeatureName/presentation/__init__.py",
            "src/$FeatureName/presentation/api/__init__.py",
            "src/$FeatureName/presentation/web/__init__.py",
            "src/$FeatureName/presentation/web/templates/base.html",
            "src/$FeatureName/presentation/web/templates/$FeatureName/readme.md",
            "src/$FeatureName/presentation/web/static/css/style.css",
            "src/$FeatureName/presentation/web/static/js/main.js",
            "src/$FeatureName/presentation/cli/__init__.py",
            "src/$FeatureName/presentation/desktop/__init__.py"
        )
    }

    Java = @{
        Common = @(
            # .vscode
            ".vscode/settings.json",
            ".vscode/launch.json",   

            # Core
            # aqui ficará tudo que é comum a todos os módulos
            "core/Errors/Failures.java",
            "core/Errors/Exceptions.java",
            "core/Utils/Constants.java",
            "core/Utils/Helpers.java",
            "core/Utils/Logging.java",

            # Root
            "pom.xml",
            "README.md",
            ".gitignore",
            ".env",
            "settings.json"
        )
        Basic = @(
            # Domain
            "src/main/java/domain/Entities/readme.md",
            "src/main/java/domain/UseCases/readme.md",
            "src/main/java/domain/Repositories/readme.md",

            # Infrastructure
            "src/main/java/infrastructure/Models/readme.md",
            "src/main/java/infrastructure/Repositories/readme.md",

            # Presentation
            "src/main/java/presentation/api/readme.md",
            "src/main/java/presentation/web/readme.md",
            "src/main/java/presentation/cli/readme.md",
            "src/main/java/presentation/desktop/readme.md"
        )
        Feature = @(
            # Domain
            "src/main/java/$FeatureName/domain/Entities/readme.md",
            "src/main/java/$FeatureName/domain/UseCases/readme.md",
            # aqui ficará as interfaces de repositórios de domínio
            # que são implementadas em infraestrutura
            "src/main/java/$FeatureName/domain/Repositories/readme.md",

            # Infrastructure
            "src/main/java/$FeatureName/infrastructure/Models/readme.md",
            "src/main/java/$FeatureName/infrastructure/Repositories/readme.md",
            
            # Presentation
            # aqui ficará as interfaces de apresentação
            "src/main/java/$FeatureName/presentation/api/readme.md",
            "src/main/java/$FeatureName/presentation/web/readme.md",
            "src/main/java/$FeatureName/presentation/cli/readme.md",
            "src/main/java/$FeatureName/presentation/desktop/readme.md"
        )
    }

    Php = @{
        Common = @(
            # .vscode
            ".vscode/settings.json",
            ".vscode/launch.json",   

            # Main
            "public/index.php",

            # Core
            # aqui ficará tudo que é comum a todos os módulos
            "core/Errors/Failures.php",
            "core/Errors/Exceptions.php",
            "core/Utils/Constants.php",
            "core/Utils/Helpers.php",
            "core/Utils/Logging.php",

            # Root
            "composer.json",
            "config/settings.php",
            "README.md",
            ".gitignore"
            ".env"
        )
        Basic = @(
            # Domain
            "src/Domain/Entities/readme.md",
            "src/Domain/UseCases/readme.md",
            "src/Domain/Repositories/readme.md",

            # Infrastructure
            "src/Infrastructure/Models/readme.md",
            "src/Infrastructure/Repositories/readme.md",

            # Presentation
            "src/Presentation/Api/readme.md",
            "src/Presentation/Web/readme.md",
            "src/Presentation/Web/Views/readme.md",
            "src/Presentation/Web/Controllers/readme.md",
            "src/Presentation/Web/Routes/readme.md",

            "src/Presentation/Cli/readme.md",
            "src/Presentation/Desktop/readme.md"
        )
        Feature = @(
            # Domain
            "src/$FeatureName/Domain/Entities/readme.md",
            "src/$FeatureName/Domain/UseCases/readme.md",
            "src/$FeatureName/Domain/Repositories/readme.md",

            # Infrastructure
            "src/$FeatureName/Infrastructure/Models/readme.md",
            "src/$FeatureName/Infrastructure/Repositories/readme.md",

            # Presentation
            "src/$FeatureName/Presentation/Api/readme.md",
            "src/$FeatureName/Presentation/Web/readme.md",
            "src/$FeatureName/Presentation/Web/Views/readme.md",
            "src/$FeatureName/Presentation/Web/Controllers/readme.md",
            "src/$FeatureName/Presentation/Web/Routes/readme.md",
            "src/$FeatureName/Presentation/Cli/readme.md",
            "src/$FeatureName/Presentation/Desktop/readme.md"
        )
    }
}

# Conteudo do .gitignore
$gitIgnoreContents = @{
    Python = @"
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
.env
.idea/
.vscode/
"@
    Java = @"
# Java
*.class
*.jar
*.war
*.ear
*.iml
.idea/
.vscode/
target/
.env
"@
    Php = @"
# PHP
/vendor/
/.env
/node_modules/
/composer.lock
.idea/
.vscode/
"@
}

# Conteúdo dos arquivos .vscode/settings.json e .vscode/launch.json
$vsCodeContents = @{
    Python = @{
        settings = @"
{

}
"@
        launch = @"
{

}
"@
    }

    Java = @{
        settings = @"
{

}
"@
        launch = @"
{

}
"@
    }

    Php = @{
        settings = @"
{

}
"@
        launch = @"
{

}
"@
    }
}

# Seleciona a estrutura baseada na linguagem escolhida
$langStructure = $baseStructures[$Language]
$fullStructure = $langStructure.Common + $langStructure.$TemplateType

# Ajusta estrutura para FeeatureName
if ($TemplateType -eq "Feature") {
}

Write-Host "Criando estrutura para:"
Write-Host "Linguagem: $Language"
Write-Host "Tipo de template: $TemplateType"

if ($TemplateType -eq "Feature") {
    Write-Host "FeatureName: $FeatureName"
}

New-Structure -structure $fullStructure

# Adiciona conteudo ao .gitignore
$gitIgnoreContents[$Language] | Out-File -FilePath ".gitignore" -Encoding utf8

# Adiciona conteudo ao .vscode/settings.json
$vsCodeContents[$Language].settings | Out-File -FilePath ".vscode/settings.json" -Encoding utf8

# Adiciona conteudo ao .vscode/launch.json
$vsCodeContents[$Language].launch | Out-File -FilePath ".vscode/launch.json" -Encoding utf8

Write-Host "`nEstrutura do projeto $Language criada com sucesso!`n"