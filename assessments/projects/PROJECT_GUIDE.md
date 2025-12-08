# BSc Blockchain, Crypto Economy & NFTs
## Semester Project Guide

**Course**: Blockchain, Crypto Economy & NFTs
**Academic Year**: 2024/2025
**Project Weight**: 70% of final grade

---

## Overview

The semester project is the central component of this course, requiring you to design, implement, and deploy a blockchain-based application. You will work in teams of 2-3 students to develop a functional decentralized application (dApp) with smart contracts, frontend interface, and comprehensive documentation.

**Project Duration**: 12 weeks (Weeks 1-12)
**Team Size**: 2-3 students
**Deliverables**: Smart contracts, frontend application, whitepaper, presentation, demo video

---

## Four Project Tracks

Choose ONE track based on your team's interests and technical skills:

### Track 1: Token Economy Track

**Description**: Design and implement a custom ERC-20 token with governance features, creating a functional token economy for a specific use case.

**Project Goals**:
- Understand token economics and governance mechanisms
- Implement secure token standards
- Create voting and governance systems
- Design sustainable tokenomics

**Minimum Requirements**:
- ERC-20 token contract with custom features (e.g., burning, minting with controls)
- Governance contract (voting on proposals, time-locks)
- Basic frontend for token interaction and voting
- Deployment on Sepolia or Polygon Mumbai testnet
- Tokenomics documentation (supply, distribution, utility)

**Suggested Features**:
- Staking mechanism with rewards
- Vesting schedules for team/investors
- Multi-signature treasury
- Quadratic voting
- Delegation mechanisms
- Token-gated access to features
- Snapshot integration for gasless voting

**Example Use Cases**:
- DAO for student organization
- Community reward token
- Decentralized content platform token
- Carbon credit tokenization
- Local community currency

**Example Deliverables**:
- Token.sol (ERC-20 implementation)
- Governance.sol (voting and proposals)
- Frontend (Next.js/React + wagmi/ethers.js)
- Whitepaper detailing tokenomics model

---

### Track 2: NFT Platform Track

**Description**: Build an NFT collection with real-world utility, going beyond simple collectibles to provide functional value.

**Project Goals**:
- Understand NFT standards and metadata
- Design utility-driven NFTs
- Implement access control and membership
- Create engaging user experiences

**Minimum Requirements**:
- ERC-721 or ERC-1155 contract with custom logic
- Metadata stored on IPFS or decentralized storage
- Minting mechanism (public sale, whitelist, or claim)
- Basic frontend for browsing and minting
- Deployment on testnet
- At least one utility feature

**Suggested Features**:
- Dynamic NFT metadata (traits change based on conditions)
- Royalty enforcement (EIP-2981)
- NFT staking for rewards
- Access-gated content (token-gating)
- Fractionalization
- NFT lending/rentals
- Trait-based rarity system
- Reveal mechanism
- Allowlist/merkle tree whitelist

**Example Use Cases**:
- Event ticketing system with transferability controls
- Membership passes (gym, co-working, clubs)
- Digital certificates and credentials
- Music NFTs with streaming rights
- Art collection with exhibition access
- Gaming items with in-game utility

**Example Deliverables**:
- NFTCollection.sol (ERC-721/1155 implementation)
- AccessControl.sol (utility management)
- Frontend (gallery, minting interface)
- Whitepaper explaining utility model

---

### Track 3: DeFi Protocol Track

**Description**: Create a simplified decentralized finance protocol, such as a lending pool, swap mechanism, or yield optimizer.

**Project Goals**:
- Understand DeFi primitives and risks
- Implement financial smart contracts
- Design economic mechanisms
- Address security concerns

**Minimum Requirements**:
- Core protocol contract (lending, swapping, or staking)
- At least 2-3 interacting contracts
- Price oracle integration (Chainlink or similar)
- Basic frontend for protocol interaction
- Deployment on testnet
- Comprehensive testing suite

**Suggested Features**:
- Flash loan functionality
- Liquidation mechanism
- Automated market maker (AMM) logic
- Yield farming/staking
- Multi-collateral support
- Fee distribution
- Governance integration
- Emergency pause mechanism

**Example Use Cases**:
- Peer-to-peer lending pool
- Simplified automated market maker (Uniswap-like)
- Yield aggregator
- Prediction market
- Decentralized insurance pool
- Staking rewards distributor

**Example Deliverables**:
- LendingPool.sol or AMM.sol
- PriceOracle.sol (oracle integration)
- RewardDistributor.sol
- Frontend (protocol dashboard)
- Whitepaper with economic model and risk analysis

**Security Note**: DeFi protocols require extra attention to security. You must include reentrancy guards, access controls, and extensive testing.

---

### Track 4: Supply Chain Track

**Description**: Develop a blockchain-based provenance tracking system for supply chain transparency and verification.

**Project Goals**:
- Understand supply chain pain points
- Design multi-stakeholder systems
- Implement role-based access control
- Create verifiable audit trails

**Minimum Requirements**:
- Product tracking contract with lifecycle stages
- Role-based permissions (manufacturer, distributor, retailer, consumer)
- Event emission for tracking history
- Basic frontend for product verification
- Deployment on testnet
- QR code or similar linking mechanism

**Suggested Features**:
- NFT-based product certificates
- Temperature/condition monitoring integration
- Multi-signature verification at stages
- Counterfeit detection
- Sustainability metrics tracking
- Batch/lot tracking
- Recall management system
- Third-party auditor role

**Example Use Cases**:
- Food supply chain (farm to table)
- Pharmaceutical tracking (authenticity)
- Luxury goods provenance (anti-counterfeiting)
- Electronics component tracking
- Fair trade certification
- Recycling and circular economy tracking

**Example Deliverables**:
- SupplyChain.sol (main tracking logic)
- AccessControl.sol (role management)
- ProductCertificate.sol (optional NFT)
- Frontend (tracking dashboard and verification)
- Whitepaper explaining use case and stakeholder benefits

---

## Project Milestones & Deliverables

### Milestone 0: Team Formation (Week 2)
**Weight**: 0% (mandatory)
**Deliverable**: Team registration form

**Requirements**:
- Form teams of 2-3 students
- Submit team composition via Moodle
- Begin initial discussions on project ideas

---

### Milestone 1: Project Proposal (Week 4)
**Weight**: 5%
**Deliverable**: 2-3 page proposal document

**Requirements**:
- Selected project track
- Problem statement and motivation
- High-level solution overview
- Target users and use cases
- Preliminary technology stack
- Team member responsibilities

**Template**: Use M1_Proposal_Template.md

**Evaluation Criteria**:
- Clarity of problem statement (30%)
- Feasibility of proposed solution (40%)
- Understanding of blockchain relevance (30%)

---

### Milestone 2: Contract Design (Week 6)
**Weight**: 10%
**Deliverable**: Technical design document + contract interfaces

**Requirements**:
- Detailed smart contract architecture
- Contract interfaces (function signatures)
- Data structures and state variables
- Interaction diagrams
- Security considerations
- Gas optimization strategy

**Template**: Use M2_Design_Template.md

**Evaluation Criteria**:
- Architectural soundness (35%)
- Completeness of design (25%)
- Security awareness (25%)
- Documentation quality (15%)

---

### Milestone 3: Core Implementation (Week 8)
**Weight**: 20%
**Deliverable**: Functional smart contracts with basic tests

**Requirements**:
- At least 2-3 smart contracts implemented
- Basic unit tests (minimum 60% coverage)
- Contract compilation without errors
- Initial deployment script
- GitHub repository with organized structure

**Template**: Use M3_Implementation_Checklist.md

**Evaluation Criteria**:
- Code functionality (40%)
- Code quality and organization (25%)
- Testing coverage (20%)
- Documentation and comments (15%)

---

### Milestone 4: Testing & Security (Week 10)
**Weight**: 15%
**Deliverable**: Comprehensive test suite + security analysis

**Requirements**:
- Unit tests with 80%+ coverage
- Integration tests for contract interactions
- Security analysis report (using Slither, Mythril, or manual review)
- Gas optimization analysis
- Edge case handling documentation

**Template**: Use M4_Security_Checklist.md

**Evaluation Criteria**:
- Test coverage and quality (40%)
- Security analysis depth (35%)
- Bug identification and fixes (25%)

---

### Milestone 5: Frontend Integration (Week 11)
**Weight**: 20%
**Deliverable**: Functional frontend application

**Requirements**:
- Web interface for contract interaction
- Wallet connection (MetaMask or similar)
- At least 3 core features accessible via UI
- Responsive design
- Error handling and user feedback
- Deployment on testnet accessible via frontend

**Evaluation Criteria**:
- Functionality and completeness (40%)
- User experience and design (25%)
- Contract integration (25%)
- Error handling (10%)

---

### Milestone 6: Final Submission (Week 12)
**Weight**: 30%
**Deliverable**: Complete project package + presentation

**Requirements**:

**1. Code & Deployment**:
- Final smart contracts on GitHub
- Deployed contracts on testnet (verified on Etherscan)
- Frontend application (deployed or runnable locally)
- Complete README with setup instructions
- All tests passing

**2. Whitepaper (8-12 pages)**:
- Executive summary
- Problem statement and motivation
- Technical architecture
- Smart contract design
- Economic model/tokenomics (if applicable)
- Security considerations
- User guide
- Future work
- References

**3. Presentation (15 minutes)**:
- Problem and solution overview
- Technical architecture
- Live demo
- Challenges and learnings
- Q&A session

**4. Demo Video (5-10 minutes)**:
- Screen recording showing full user flow
- Voiceover explanation
- Uploaded to YouTube/Vimeo

**Template**: Use M6_Final_Submission_Checklist.md

**Evaluation Criteria**:
- Technical implementation (35%)
- Documentation quality (20%)
- Presentation clarity (15%)
- Demo effectiveness (10%)
- Code quality and security (20%)

---

## Technical Requirements

### Smart Contracts
- **Language**: Solidity 0.8.x
- **Development Framework**: Hardhat or Foundry
- **Testing**: Chai/Mocha or Forge
- **Standards**: Follow OpenZeppelin implementations where applicable
- **Documentation**: NatSpec comments for all public functions

### Frontend
- **Framework**: React, Next.js, or Vue.js
- **Web3 Library**: ethers.js or wagmi
- **Wallet**: MetaMask integration required
- **Hosting**: Vercel, Netlify, GitHub Pages, or IPFS

### Deployment
- **Network**: Sepolia, Polygon Mumbai, or Arbitrum Goerli testnet
- **Verification**: Contract verification on block explorer
- **Faucet**: Provide faucet links in documentation

### Repository
- **Platform**: GitHub (public repository)
- **Structure**: Organized folders (contracts/, frontend/, tests/, docs/)
- **README**: Clear setup and deployment instructions
- **License**: Include open-source license (MIT recommended)

---

## Grading Breakdown (Project: 70% of Course Grade)

| Component | Weight |
|-----------|--------|
| M1: Project Proposal | 5% |
| M2: Contract Design | 10% |
| M3: Core Implementation | 20% |
| M4: Testing & Security | 15% |
| M5: Frontend Integration | 20% |
| M6: Final Submission | 30% |
| **Total** | **100%** |

See RUBRICS.md for detailed grading criteria.

---

## Best Practices

### Development
- Start simple, iterate to complexity
- Commit code frequently to GitHub
- Write tests as you develop
- Document design decisions
- Use version control branching effectively

### Security
- Never deploy to mainnet without professional audit
- Use OpenZeppelin libraries for standards
- Implement access controls
- Add reentrancy guards where needed
- Test edge cases and failure modes
- Use SafeMath or Solidity 0.8+ overflow protection

### Collaboration
- Define clear roles within team
- Communicate regularly via Slack/Discord
- Review each other's code
- Share knowledge and learning
- Ask for help early if blocked

### Documentation
- Write clear commit messages
- Document contract functions with NatSpec
- Maintain updated README
- Include setup instructions for reproducibility
- Explain design trade-offs

---

## Resources

### Learning Materials
- Course lecture slides and recordings
- Lab assignments as building blocks
- OpenZeppelin documentation
- Ethereum.org developer resources
- Solidity by Example

### Development Tools
- Hardhat: https://hardhat.org
- Foundry: https://getfoundry.sh
- Remix IDE: https://remix.ethereum.org
- OpenZeppelin Contracts: https://github.com/OpenZeppelin/openzeppelin-contracts
- Ethers.js: https://docs.ethers.org

### Testing Tools
- Hardhat Test Framework
- Waffle (Ethereum testing)
- Foundry Forge
- Tenderly (debugging)

### Security Tools
- Slither (static analysis)
- Mythril (symbolic execution)
- OpenZeppelin Defender
- Etherscan contract verification

### Frontend Tools
- wagmi: https://wagmi.sh
- RainbowKit: https://rainbowkit.com
- Web3Modal: https://web3modal.com

---

## Academic Integrity

- All code must be original or properly attributed
- You may use OpenZeppelin libraries and standard implementations
- Cite any external resources, tutorials, or code snippets
- Plagiarism will result in project failure and academic consequences
- Collaboration between teams is not allowed; work only with your team members

---

## Support & Office Hours

- **Instructor Office Hours**: [Insert schedule]
- **TA Support**: [Insert schedule]
- **Discussion Forum**: Moodle/Slack channel
- **Email**: [Insert contact]

---

## Important Dates

| Milestone | Due Date | Weight |
|-----------|----------|--------|
| M0: Team Formation | Week 2 | 0% |
| M1: Proposal | Week 4 | 5% |
| M2: Design | Week 6 | 10% |
| M3: Implementation | Week 8 | 20% |
| M4: Security | Week 10 | 15% |
| M5: Frontend | Week 11 | 20% |
| M6: Final Submission | Week 12 | 30% |

**Late Policy**: 10% deduction per day, maximum 3 days late. After 3 days, submissions will not be accepted.

---

## FAQ

**Q: Can we switch tracks after M1?**
A: Track changes are allowed until M2 submission, but require instructor approval.

**Q: What if our team has issues?**
A: Contact the instructor immediately. We can facilitate mediation or team adjustments if necessary.

**Q: Can we use AI coding assistants?**
A: Yes, but you must understand all generated code and be able to explain it during presentations.

**Q: How much code is expected?**
A: Quality over quantity. Typical projects have 300-800 lines of Solidity and a functional frontend.

**Q: What if we find a bug after final submission?**
A: Document known issues in your whitepaper. Critical bugs found during presentation may impact grade.

---

**Good luck with your projects! Build something you're proud of.**
