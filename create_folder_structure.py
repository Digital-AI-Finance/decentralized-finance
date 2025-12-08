"""
Create folder structure for BSc Blockchain Course
48 lessons x 45 min = 36 hours
Organized by 7 modules (A-G)
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(r"D:\Joerg\Research\slides\Blockchain_Crypto")

# All 48 lessons organized by module
MODULES = {
    "Module_A_Blockchain_Foundations": [
        ("L01", "What_is_Blockchain", "Lecture"),
        ("L02", "DLT_Concepts", "Lecture"),
        ("L03", "Hash_Functions", "Lecture"),
        ("L04", "Lab_Hash_Experiments", "Lab"),
        ("L05", "Public_Key_Cryptography", "Lecture"),
        ("L06", "Bitcoin_Protocol", "Lecture"),
        ("L07", "Proof_of_Work", "Lecture"),
        ("L08", "Lab_Wallet_Setup", "Lab"),
        ("L09", "Proof_of_Stake", "Lecture"),
        ("L10", "Consensus_Comparison", "Lecture"),
        ("L11", "Scalability_Trilemma", "Lecture"),
        ("L12", "Lab_Block_Explorer", "Lab"),
    ],
    "Module_B_Ethereum_Smart_Contracts": [
        ("L13", "Ethereum_Architecture", "Lecture"),
        ("L14", "Gas_Mechanics", "Lecture"),
        ("L15", "Smart_Contract_Fundamentals", "Lecture"),
        ("L16", "Lab_Interacting_Contracts", "Lab"),
        ("L17", "ERC20_Token_Standard", "Lecture"),
        ("L18", "ERC721_ERC1155_NFT_Standards", "Lecture"),
        ("L19", "Token_Lifecycle", "Lecture"),
        ("L20", "Lab_Token_Analysis", "Lab"),
    ],
    "Module_C_NFTs_Digital_Assets": [
        ("L21", "NFT_Technology_Deep_Dive", "Lecture"),
        ("L22", "NFT_Metadata_IPFS", "Lecture"),
        ("L23", "NFT_Marketplaces", "Lecture"),
        ("L24", "Lab_OpenSea_Analysis", "Lab"),
        ("L25", "Digital_Art_Collectibles", "Lecture"),
        ("L26", "Gaming_NFTs_Metaverse", "Lecture"),
        ("L27", "RWA_Tokenization", "Lecture"),
        ("L28", "Lab_NFT_Evaluation", "Lab"),
    ],
    "Module_D_Tokenomics": [
        ("L29", "Token_Economics", "Lecture"),
        ("L30", "Distribution_Vesting", "Lecture"),
        ("L31", "Token_Types", "Lecture"),
        ("L32", "Lab_Tokenomics_Analysis", "Lab"),
    ],
    "Module_E_DeFi_Ecosystem": [
        ("L33", "Intro_DeFi", "Lecture"),
        ("L34", "AMM_Mechanics", "Lecture"),
        ("L35", "Uniswap_Deep_Dive", "Lecture"),
        ("L36", "Lab_Testnet_Swap", "Lab"),
        ("L37", "Lending_Protocols", "Lecture"),
        ("L38", "Stablecoin_Mechanisms", "Lecture"),
        ("L39", "Case_Study_Terra_Luna", "Lecture"),
        ("L40", "Lab_Testnet_Lending", "Lab"),
    ],
    "Module_F_Advanced_Topics": [
        ("L41", "Layer2_Scaling", "Lecture"),
        ("L42", "Flash_Loans_Composability", "Lecture"),
        ("L43", "Smart_Contract_Security", "Lecture"),
        ("L44", "Lab_Security_Audit", "Lab"),
    ],
    "Module_G_Regulation_Future": [
        ("L45", "Global_Regulatory_Landscape", "Lecture"),
        ("L46", "Swiss_FINMA_MiCA", "Lecture"),
        ("L47", "Future_Trends", "Lecture"),
        ("L48", "Course_Synthesis", "Lecture"),
    ],
}

def create_structure():
    """Create the complete folder structure."""

    # Create base directories
    dirs_to_create = [
        BASE_DIR / "syllabus",
        BASE_DIR / "assessments" / "assignment1_blockchain_exploration",
        BASE_DIR / "assessments" / "assignment2_nft_token_analysis",
        BASE_DIR / "assessments" / "assignment3_defi_analysis",
        BASE_DIR / "assessments" / "midterm",
        BASE_DIR / "assessments" / "final_project",
        BASE_DIR / "resources",
        BASE_DIR / "charts",  # Shared chart library
        BASE_DIR / "temp",
        BASE_DIR / "previous",
    ]

    for d in dirs_to_create:
        d.mkdir(parents=True, exist_ok=True)
        print(f"Created: {d}")

    # Create module folders with lesson subfolders
    total_lessons = 0
    for module_name, lessons in MODULES.items():
        module_dir = BASE_DIR / module_name
        module_dir.mkdir(parents=True, exist_ok=True)
        print(f"\nModule: {module_dir}")

        for lesson_id, lesson_name, lesson_type in lessons:
            lesson_folder = f"{lesson_id}_{lesson_name}"
            lesson_dir = module_dir / lesson_folder

            # Create lesson folder with subfolders
            lesson_dir.mkdir(parents=True, exist_ok=True)
            (lesson_dir / "charts").mkdir(parents=True, exist_ok=True)
            (lesson_dir / "previous").mkdir(parents=True, exist_ok=True)

            # Create placeholder files
            if lesson_type == "Lab":
                lab_guide = lesson_dir / "lab_guide.md"
                lab_guide.write_text(f"# {lesson_name.replace('_', ' ')}\n\n## Objectives\n\n## Instructions\n\n## Expected Output\n", encoding='utf-8')

            total_lessons += 1
            print(f"  {lesson_folder} ({lesson_type})")

    # Create README.md
    readme_content = """# BSc Blockchain, Crypto Economy, and NFTs

## Course Overview
- **Duration:** 48 lessons x 45 min = 36 hours
- **Structure:** 7 modules (A-G)
- **Prerequisites:** None

## Module Structure

### Module A: Blockchain Foundations (Lessons 1-12)
Core blockchain concepts, cryptography, Bitcoin, consensus mechanisms

### Module B: Ethereum & Smart Contracts (Lessons 13-20)
Ethereum architecture, gas, token standards

### Module C: NFTs & Digital Assets (Lessons 21-28)
NFT technology, marketplaces, applications, valuation

### Module D: Tokenomics (Lessons 29-32)
Token economics, distribution, token types

### Module E: DeFi Ecosystem (Lessons 33-40)
AMMs, lending, stablecoins, case studies

### Module F: Advanced Topics (Lessons 41-44)
Layer 2, flash loans, security

### Module G: Regulation & Future (Lessons 45-48)
Global regulation, Swiss FINMA, MiCA, future trends

## Folder Structure
Each lesson folder contains:
- `YYYYMMDD_HHMM_L##_title.tex` - Beamer slides
- `charts/` - Lesson-specific visualizations
- `lab_guide.md` (for lab lessons only)
- `previous/` - Version history
"""

    readme_path = BASE_DIR / "README.md"
    readme_path.write_text(readme_content, encoding='utf-8')
    print(f"\nCreated: {readme_path}")

    print("\n" + "="*60)
    print("Folder structure created successfully!")
    print(f"Base directory: {BASE_DIR}")
    print(f"Total modules: {len(MODULES)}")
    print(f"Total lessons: {total_lessons}")
    print("="*60)

if __name__ == "__main__":
    create_structure()
