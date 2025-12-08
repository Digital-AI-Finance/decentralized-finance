"""
Create folder structure for BSc Blockchain, Crypto Economy & NFTs course
"""
from pathlib import Path

# Base directory
base_dir = Path(__file__).parent

# Define folder structure
folders = [
    # Module A - Blockchain Foundations
    "Module_A_Blockchain_Foundations/L01_What_is_Blockchain",
    "Module_A_Blockchain_Foundations/L02_DLT_Concepts",
    "Module_A_Blockchain_Foundations/L03_Hash_Functions",
    "Module_A_Blockchain_Foundations/L04_Lab_Hash_Experiments",
    "Module_A_Blockchain_Foundations/L05_Public_Key_Cryptography",
    "Module_A_Blockchain_Foundations/L06_Bitcoin_Protocol",
    "Module_A_Blockchain_Foundations/L07_Proof_of_Work",
    "Module_A_Blockchain_Foundations/L08_Lab_Wallet_Setup",
    "Module_A_Blockchain_Foundations/L09_Proof_of_Stake",
    "Module_A_Blockchain_Foundations/L10_Consensus_Comparison",
    "Module_A_Blockchain_Foundations/L11_Scalability_Trilemma",
    "Module_A_Blockchain_Foundations/L12_Lab_Block_Explorer",

    # Module B - Ethereum & Smart Contracts
    "Module_B_Ethereum_Smart_Contracts/L13_Ethereum_Architecture",
    "Module_B_Ethereum_Smart_Contracts/L14_Gas_Mechanics",
    "Module_B_Ethereum_Smart_Contracts/L15_Solidity_Fundamentals",
    "Module_B_Ethereum_Smart_Contracts/L16_Lab_Contract_Interaction",
    "Module_B_Ethereum_Smart_Contracts/L17_ERC20_Token_Standard",
    "Module_B_Ethereum_Smart_Contracts/L18_ERC721_ERC1155_NFT_Standards",
    "Module_B_Ethereum_Smart_Contracts/L19_Token_Lifecycle",
    "Module_B_Ethereum_Smart_Contracts/L20_Lab_Token_Analysis",

    # Module C - NFTs & Digital Assets
    "Module_C_NFTs_Digital_Assets/L21_NFT_Technology_Deep_Dive",
    "Module_C_NFTs_Digital_Assets/L22_NFT_Metadata_IPFS",
    "Module_C_NFTs_Digital_Assets/L23_NFT_Marketplaces",
    "Module_C_NFTs_Digital_Assets/L24_Lab_OpenSea_Analysis",
    "Module_C_NFTs_Digital_Assets/L25_Digital_Art_Collectibles",
    "Module_C_NFTs_Digital_Assets/L26_Gaming_NFTs_Metaverse",
    "Module_C_NFTs_Digital_Assets/L27_RWA_Tokenization",
    "Module_C_NFTs_Digital_Assets/L28_Lab_NFT_Valuation",

    # Module D - Tokenomics
    "Module_D_Tokenomics/L29_Token_Economics_Fundamentals",
    "Module_D_Tokenomics/L30_Distribution_Vesting",
    "Module_D_Tokenomics/L31_Token_Classification_Valuation",
    "Module_D_Tokenomics/L32_Lab_Tokenomics_Analysis",

    # Module E - DeFi Ecosystem
    "Module_E_DeFi_Ecosystem/L33_Introduction_to_DeFi",
    "Module_E_DeFi_Ecosystem/L34_AMM_Mechanics",
    "Module_E_DeFi_Ecosystem/L35_Uniswap_Deep_Dive",
    "Module_E_DeFi_Ecosystem/L36_Lab_Testnet_Swap",
    "Module_E_DeFi_Ecosystem/L37_Lending_Protocols",
    "Module_E_DeFi_Ecosystem/L38_Stablecoin_Mechanisms",
    "Module_E_DeFi_Ecosystem/L39_Case_Study_Terra_Luna",
    "Module_E_DeFi_Ecosystem/L40_Lab_Testnet_Lending",

    # Module F - Advanced Topics
    "Module_F_Advanced_Topics/L41_Layer2_Scaling",
    "Module_F_Advanced_Topics/L42_Flash_Loans_Composability",
    "Module_F_Advanced_Topics/L43_Smart_Contract_Security",
    "Module_F_Advanced_Topics/L44_Lab_Security_Audit",

    # Module G - Regulation & Future
    "Module_G_Regulation_Future/L45_Global_Regulatory_Landscape",
    "Module_G_Regulation_Future/L46_Swiss_FINMA_EU_MiCA",
    "Module_G_Regulation_Future/L47_CBDCs_Future_Trends",
    "Module_G_Regulation_Future/L48_Course_Synthesis",

    # Supporting folders
    "assessments/projects",
    "assessments/quizzes",
    "assessments/rubrics",
    "labs",
    "charts",
]

# Create all folders
created = []
already_exists = []

for folder in folders:
    folder_path = base_dir / folder
    if not folder_path.exists():
        folder_path.mkdir(parents=True, exist_ok=True)
        created.append(folder)
    else:
        already_exists.append(folder)

# Report results
print("=" * 80)
print("FOLDER STRUCTURE CREATION REPORT")
print("=" * 80)
print(f"\nCreated {len(created)} new folders:")
for f in created:
    print(f"  + {f}")

if already_exists:
    print(f"\n{len(already_exists)} folders already existed:")
    for f in already_exists[:5]:  # Show first 5
        print(f"  - {f}")
    if len(already_exists) > 5:
        print(f"  ... and {len(already_exists) - 5} more")

print(f"\nTotal folders: {len(folders)}")
print("\nBase directory:", base_dir)
print("=" * 80)
