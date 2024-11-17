# OKX Sender

Этот скрипт осуществляет автоматическую рассылку с биржи OKX на указанные кошельки с настраиваемой задержкой.

## Установка

### 1. Создайте виртуальное окружение

Для начала создайте виртуальное окружение, используя `virtualenv`:

```bash

virtualenv venv --python=python3.11

```

2. Активируйте виртуальное окружение

```bash

venv\Scripts\activate

```

3. Установите зависимости

Установите необходимые пакеты из requirements.txt:

```bash

pip install -r requirements.txt

```

4. Запуск скрипта

Для запуска скрипта используйте команду:

```bash

python run.py

```

## Настройка

После первого запуска скрипта автоматически создастся папка files, файл settings.json и wallets.txt.

settings.json В этом файле укажите все необходимые параметры для корректной работы скрипта.

wallets.txt - Укажите ваши кошельки для рассылки. (Убедитесь что они добавлены в список разрешённых аккаунтов и подтверждены в вашем аккаунте OKX).

### Использование

В файл files/settings.json укажите настройки. Есть возможность дождаться желаемой комиссии за вывод введя в поле max_fee нужную цифру, либо оставьте false.

Зайдите в файл main.py и в переменную TOKEN_SYMBOL введите токен для вывода, а в CHAIN выберете нужную сеть, чтобы получилось Chains.SOL или другая выбранная сеть.

Список поддерживаемых сетей:
```
    AELF = 'AELF'
    Acala = 'Acala'
    Algorand = 'Algorand'
    Aptos = 'Aptos'
    ArbitrumOne = 'Arbitrum One'
    ArbitrumOneBridged = 'Arbitrum One (Bridged)'
    Arweave = 'Arweave'
    Astar = 'Astar'
    AvalancheCChain = 'Avalanche C-Chain'
    AvalancheXChain = 'Avalanche X-Chain'
    BRC20 = 'BRC20'
    BSC = 'BSC'
    Bitcoin = 'Bitcoin'
    BitcoinSV = 'Bitcoin SV'
    BitcoinCash = 'BitcoinCash'
    Bytom = 'Bytom'
    CELO = 'CELO'
    CELOTOKEN = 'CELO-TOKEN'
    CFX_EVM = 'CFX_EVM'
    CORE = 'CORE'
    Cardano = 'Cardano'
    Casper = 'Casper'
    Chia = 'Chia'
    ChilizLegacyChain = 'Chiliz Legacy Chain'
    Conflux = 'Conflux'
    Cortex = 'Cortex'
    Cosmos = 'Cosmos'
    Crypto = 'Crypto'
    Decred = 'Decred'
    Dfinity = 'Dfinity'
    Digibyte = 'Digibyte'
    DigitalCash = 'Digital Cash'
    Dogecoin = 'Dogecoin'
    EOS = 'EOS'
    ERC20 = 'ERC20'
    Elrond = 'Elrond'
    Eminer = 'Eminer'
    EthereumClassic = 'Ethereum Classic'
    EthereumPoW = 'EthereumPoW'
    FEVM = 'FEVM'
    FLOW = 'FLOW'
    Fantom = 'Fantom'
    Filecoin = 'Filecoin'
    Flare = 'Flare'
    Fusion = 'Fusion'
    Harmony = 'Harmony'
    Hedera = 'Hedera'
    Horizen = 'Horizen'
    HyperCash = 'HyperCash'
    ICON = 'ICON'
    INTCHAIN = 'INTCHAIN'
    IOST = 'IOST'
    KAR = 'KAR'
    Kadena = 'Kadena'
    Khala = 'Khala'
    Klaytn = 'Klaytn'
    Kusama = 'Kusama'
    Lightning = 'Lightning'
    Linkeye = 'Linkeye'
    Lisk = 'Lisk'
    Litecoin = 'Litecoin'
    MIOTA = 'MIOTA'
    Metis = 'Metis'
    Mina = 'Mina'
    Monero = 'Monero'
    Moonbeam = 'Moonbeam'
    Moonriver = 'Moonriver'
    N3 = 'N3'
    NEAR = 'NEAR'
    NEO = 'NEO'
    NULS = 'NULS'
    Nano = 'Nano'
    NewEconomyMovement = 'New Economy Movement'
    OASYS = 'OASYS'
    OKTC = 'OKTC'
    OmegaChain = 'Omega Chain'
    Ontology = 'Ontology'
    Optimism = 'Optimism'
    OptimismBridged = 'Optimism (Bridged)'
    OptimismV1 = 'Optimism (V1)'
    OptimismV2 = 'Optimism (V2)'
    PlatON = 'PlatON'
    Polkadot = 'Polkadot'
    Polygon = 'Polygon'
    Quantum = 'Quantum'
    Ravencoin = 'Ravencoin'
    Ripple = 'Ripple'
    Ronin = 'Ronin'
    SUI = 'SUI'
    Siacoin = 'Siacoin'
    Solana = 'Solana'
    Starknet = 'Starknet'
    StellarLumens = 'Stellar Lumens'
    StepNetwork = 'Step Network'
    TON = 'TON'
    TRC20 = 'TRC20'
    Terra = 'Terra'
    TerraClassic = 'Terra Classic'
    Tezos = 'Tezos'
    Theta = 'Theta'
    UMEE = 'UMEE'
    VSYSTEMS = 'VSYSTEMS'
    WAVES = 'WAVES'
    WGRT = 'WGRT'
    Wax = 'Wax'
    XANA = 'XANA'
    XEC = 'XEC'
    Zcash = 'Zcash'
    Zilliqa = 'Zilliqa'
    lStacks = 'l-Stacks'
    zkSyncEra = 'zkSync Era'
    zkSyncLite = 'zkSync Lite'
```

После настройки settings.json вы можете снова запустить скрипт с помощью:

```bash

python run.py

```

Скрипт автоматически выполнит рассылку на указанные кошельки.