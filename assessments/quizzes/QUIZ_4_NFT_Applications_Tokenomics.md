# Quiz 4: NFT Applications & Tokenomics
## BSc Blockchain, Crypto Economy & NFTs

**Lectures Covered**: L25-L32 (NFT Use Cases through Tokenomics Design)
**Duration**: 30 minutes
**Total Points**: 100 points
**Question Types**: 6 multiple choice (8 pts each), 4 short answer (13 pts each)

---

## Multiple Choice Questions (48 points total)

### Question 1 (8 points)
**Topic**: NFT Use Cases

Which of the following is NOT a common real-world use case for NFTs?

A) Digital art ownership and provenance
B) Event ticketing with transfer controls
C) Currency for everyday transactions
D) Gaming items and virtual real estate

**Correct Answer**: C

**Explanation**: NFTs are non-fungible (unique) and therefore not suitable for everyday currency transactions, which require fungible units of equal value. NFTs excel at representing unique items: art, tickets, gaming assets, credentials, memberships, real estate (both virtual and tokenized physical).

---

### Question 2 (8 points)
**Topic**: Token Utility

What does "token utility" refer to in the context of tokenomics?

A) The physical usefulness of a blockchain token
B) The functional purpose and benefits that a token provides within its ecosystem
C) The mining difficulty of a token
D) The energy efficiency of token transactions

**Correct Answer**: B

**Explanation**: Token utility refers to the actual use cases and benefits a token provides within its ecosystem. Examples include: governance rights, access to services, staking rewards, fee discounts, collateral, or in-game currency. Strong utility creates demand for the token beyond speculation.

---

### Question 3 (8 points)
**Topic**: Token Distribution

Which token distribution mechanism is designed to reward early adopters and community members for contributing to protocol growth?

A) Initial Coin Offering (ICO)
B) Airdrop
C) Proof of Work mining
D) Token burning

**Correct Answer**: B

**Explanation**: Airdrops distribute tokens for free (or based on criteria) to community members, often rewarding early adopters, active users, or governance participants. ICOs sell tokens for fundraising. Mining distributes based on computational work. Burning removes tokens from supply.

---

### Question 4 (8 points)
**Topic**: Governance Tokens

What is the primary purpose of governance tokens in a DAO (Decentralized Autonomous Organization)?

A) To pay transaction fees
B) To enable token holders to vote on protocol decisions and proposals
C) To generate passive income through staking
D) To serve as collateral for loans

**Correct Answer**: B

**Explanation**: Governance tokens grant voting rights, allowing holders to participate in decision-making about protocol changes, treasury allocation, parameter adjustments, and strategic direction. While governance tokens may also have other utilities (staking, fees), their primary purpose is decentralized governance.

---

### Question 5 (8 points)
**Topic**: NFT Fractionalization

What is NFT fractionalization?

A) Breaking an NFT into smaller, divisible pieces represented by fungible tokens
B) Creating multiple copies of an NFT
C) Reducing the price of an NFT
D) Splitting royalties among multiple creators

**Correct Answer**: A

**Explanation**: Fractionalization converts a single NFT (e.g., expensive artwork) into many fungible ERC-20 tokens representing fractional ownership. This enables: shared ownership, price discovery, liquidity for high-value NFTs, and broader accessibility. Each fraction holder owns a proportional claim to the underlying NFT.

---

### Question 6 (8 points)
**Topic**: Token Supply Models

What is the difference between "circulating supply" and "total supply" in tokenomics?

A) There is no difference; they are the same
B) Circulating supply is tokens actively available for trading; total supply includes locked, vested, or reserved tokens
C) Total supply is always smaller than circulating supply
D) Circulating supply only counts tokens held by the team

**Correct Answer**: B

**Explanation**: Circulating supply represents tokens publicly available and tradeable in the market. Total supply includes all minted tokens, including those locked in vesting schedules, team allocations, treasury reserves, or staking contracts. Circulating supply increases over time as locked tokens are released.

---

## Short Answer Questions (52 points total)

### Question 7 (13 points)
**Topic**: NFT Royalties

Explain how NFT royalties work on secondary sales. What are the technical challenges in enforcing royalties, and how have marketplaces addressed this issue?

**Model Answer** (for grading reference):

**How NFT Royalties Work**:

NFT royalties allow creators to receive a percentage of sales every time their NFT is resold on secondary markets. For example, an artist sets a 10% royalty - when their NFT sells for 1 ETH on OpenSea, the artist automatically receives 0.1 ETH.

**Technical Implementation**:
- EIP-2981 standardizes royalty information storage
- Contract implements royaltyInfo(tokenId, salePrice) function
- Returns: royalty recipient address and royalty amount
- Marketplaces query this function and route payments accordingly

**Technical Challenges**:

1. **Not Enforceable On-Chain**:
   - Royalties depend on marketplace cooperation - they're not enforced by the NFT contract itself
   - Direct wallet-to-wallet transfers bypass royalties entirely
   - Marketplaces can choose to ignore royalty information

2. **Standardization**:
   - Different marketplaces historically used different royalty standards
   - EIP-2981 provides standard but isn't universally adopted on older contracts

3. **P2P Transfers**:
   - Users can transfer NFTs directly via transferFrom() without triggering royalty payments
   - No on-chain mechanism to force royalties on all transfers

**How Marketplaces Address This**:

1. **Voluntary Honor System** (Traditional Approach):
   - Marketplaces like OpenSea, Rarible read royalty info and honor it
   - Creates expectation and social pressure
   - Limited enforcement

2. **Operator Filtering** (Newer Approach):
   - Royalty enforcement contracts (e.g., OpenSea's Operator Filter Registry)
   - Contracts can block transfers through non-compliant marketplaces
   - Overrides transferFrom() to check approved operators
   - Controversial: limits composability

3. **Hybrid Models**:
   - Optional royalties with creator choice
   - Tiered royalty rates
   - Royalty sharing with platform

**Recent Developments**:
Some major marketplaces (like Blur) moved to optional royalties, creating tension between creator revenue and market competition. This led to debates about "creator fees" vs true "royalties."

**Grading Criteria**:
- 13 points: Explains mechanism, identifies challenges, describes solutions comprehensively
- 9-12 points: Good explanation but missing some details
- 6-8 points: Basic understanding but incomplete
- 3-5 points: Vague or partially incorrect
- 0-2 points: Incorrect or no meaningful answer

---

### Question 8 (13 points)
**Topic**: Tokenomics Design

Design a simple tokenomics model for a hypothetical decentralized social media platform. Include: token utility, distribution mechanism, and at least one incentive mechanism to encourage user participation.

**Model Answer** (for grading reference):

**Example: "SocialChain" - Decentralized Social Media Platform**

**Token**: SOCIAL (ERC-20)

**Token Utility** (how tokens are used):
1. **Governance**: Vote on content moderation policies, feature proposals, treasury allocation
2. **Content Boosting**: Spend tokens to promote posts to wider audiences
3. **Premium Features**: Access to analytics, verification badges, ad-free experience
4. **Creator Tipping**: Direct payments to content creators
5. **Staking**: Stake tokens to become a content moderator and earn fees

**Distribution Mechanism** (10 billion total supply):
- 30% (3B): Community rewards (released over 5 years via user incentives)
- 20% (2B): Team and advisors (4-year vesting with 1-year cliff)
- 15% (1.5B): Investors (3-year vesting)
- 20% (2B): Treasury (DAO-controlled for grants, partnerships)
- 10% (1B): Liquidity mining (incentivize DEX liquidity)
- 5% (0.5B): Initial airdrop to early users

**Incentive Mechanisms**:

1. **Content Creation Rewards**:
   - Users earn SOCIAL tokens based on engagement (likes, shares, comments)
   - Quadratic rewards to prevent spam (diminishing returns)
   - Quality threshold: content must meet minimum engagement to earn

2. **Curation Rewards**:
   - Early upvoters of popular content earn tokens
   - Incentivizes quality discovery and reduces spam

3. **Moderation Staking**:
   - Stake 10,000 SOCIAL to become moderator
   - Earn portion of platform fees
   - Slashed if flagged for biased moderation

4. **Engagement Mining**:
   - Active users (posting, commenting, sharing) earn daily token rewards
   - Anti-bot measures: wallet age, activity patterns

**Supply Controls**:
- Token burning: 10% of advertising revenue used to buy back and burn tokens
- Inflation: Max 2% annual inflation for ongoing community rewards
- Deflationary pressure from feature usage (tokens spent on boosts are burned)

**Economic Sustainability**:
- Revenue streams: advertising (paid in SOCIAL or ETH), premium subscriptions, NFT marketplace fees
- Portion of revenue funds rewards pool
- Treasury can adjust reward rates based on token price and participation

**Grading Criteria**:
- 13 points: Complete model with clear utility, distribution, incentives, and economic thinking
- 9-12 points: Good model but missing some elements or less detailed
- 6-8 points: Basic model with significant gaps
- 3-5 points: Incomplete or poorly thought out
- 0-2 points: Does not constitute a meaningful tokenomics model

---

### Question 9 (13 points)
**Topic**: Dynamic NFTs

What are "dynamic NFTs" and how do they differ from traditional static NFTs? Provide two specific use cases where dynamic NFTs would be preferable.

**Model Answer** (for grading reference):

**Dynamic NFTs** (dNFTs):

NFTs whose metadata or properties change over time based on external events, user actions, or on-chain/off-chain data. Unlike static NFTs with immutable metadata, dynamic NFTs evolve and adapt.

**How They Differ from Static NFTs**:

**Static NFTs**:
- Metadata set at minting and never changes
- Image, attributes, and properties are permanent
- TokenURI points to fixed JSON file
- Example: CryptoPunk 1234 looks the same forever

**Dynamic NFTs**:
- Metadata updates based on conditions or triggers
- Visual appearance, attributes, or statistics can change
- TokenURI may point to on-chain data or updatable source
- Smart contract contains logic for updates
- Often use Chainlink oracles for external data

**Technical Implementation**:
```solidity
contract DynamicNFT is ERC721 {
    mapping(uint256 => Stats) public tokenStats;

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        Stats memory stats = tokenStats[tokenId];
        // Generate JSON based on current stats
        return generateMetadata(stats);
    }

    function updateStats(uint256 tokenId, uint256 newScore) external {
        // Update based on game events, oracle data, etc.
        tokenStats[tokenId].score = newScore;
    }
}
```

**Use Cases**:

**Use Case 1: Gaming Characters**
- NFT represents a game character
- Attributes (level, experience, health, equipment) change as player progresses
- Visual appearance evolves with level-ups or achievements
- Items collected appear on the character
- Damage or victories recorded on-chain
- Example: Character starts as level 1 warrior, evolves to level 50 mage with legendary armor
- Benefits: True ownership of progression, transferable gaming achievements

**Use Case 2: Real-World Asset Tracking**
- NFT represents a physical asset (e.g., luxury watch, wine bottle)
- Attributes update based on real-world events:
  - Location changes (supply chain tracking)
  - Ownership history (provenance)
  - Condition reports (from authenticated inspections)
  - Valuation updates (from oracle price feeds)
- Temperature/humidity logs for sensitive goods (wine, art)
- Example: Wine NFT updates vintage rating, storage conditions, and market value over time
- Benefits: Dynamic provenance, insurance integration, authenticity verification

**Use Case 3: Environmental Impact NFTs**
- Carbon credit NFTs that update based on verified emissions reductions
- Forest conservation NFTs showing real-time satellite data of protected areas
- Renewable energy certificates updating with production data
- Example: Tree planting NFT shows growth progress via satellite imagery
- Benefits: Transparency, verifiable impact, prevents double-counting

**Use Case 4: Financial NFTs**
- NFT bonds with changing attributes (interest accrued, maturity countdown)
- Loan NFTs showing repayment status
- Insurance policy NFTs reflecting claim history
- Example: Bond NFT updates face value, accrued interest, days to maturity
- Benefits: Real-time financial tracking, tradeable debt instruments

**Oracle Integration**:
Dynamic NFTs often use Chainlink oracles to:
- Fetch external data (weather, sports scores, asset prices)
- Trigger updates based on real-world events
- Verify off-chain computations

**Grading Criteria**:
- 13 points: Clear explanation of concept + 2 detailed, appropriate use cases
- 9-12 points: Good explanation but use cases less developed
- 6-8 points: Basic understanding but incomplete
- 3-5 points: Vague or poor use cases
- 0-2 points: Incorrect or no meaningful answer

---

### Question 10 (13 points)
**Topic**: Token Vesting

Explain what token vesting is and why it's important in tokenomics. Describe a typical vesting schedule for team tokens and explain the purpose of a "cliff."

**Model Answer** (for grading reference):

**Token Vesting**:

Vesting is the gradual release of tokens over time rather than all at once. Recipients have allocation rights but cannot access or sell tokens until they vest according to a predetermined schedule. This aligns long-term incentives and prevents immediate sell pressure.

**Why Vesting is Important**:

1. **Prevents Immediate Dumping**:
   - Without vesting, team/investors could sell all tokens immediately after launch
   - Massive sell pressure crashes token price
   - Harms community and project credibility

2. **Aligns Long-Term Incentives**:
   - Team members must stay committed to project success
   - Token value remains tied to future performance
   - Reduces "pump and dump" risk

3. **Fair Distribution**:
   - Community gets tokens before insiders can sell
   - Prevents immediate wealth extraction by early participants
   - Creates more equitable market dynamics

4. **Builds Trust**:
   - Transparent vesting schedules demonstrate commitment
   - Investors see team has "skin in the game"
   - Reduces rug pull risk

**Typical Team Vesting Schedule**:

**Example: 4-year vesting with 1-year cliff**

- **Total Allocation**: 2 million tokens (20% of supply)
- **Cliff**: 1 year
- **Vesting Period**: 4 years total
- **Vesting Frequency**: Monthly (after cliff)

**Timeline**:
- Month 0-12: 0 tokens released (cliff period)
- Month 12: 500,000 tokens released (25% of allocation)
- Month 13-48: ~41,667 tokens/month (remaining 75% over 36 months)
- Month 48: All tokens fully vested

**Purpose of the Cliff**:

The cliff is an initial period (typically 6-12 months) where NO tokens vest at all.

**Why Cliffs Exist**:

1. **Commitment Test**:
   - Ensures team members stay for minimum viable period
   - If someone leaves before cliff, they get zero tokens
   - Creates strong retention incentive

2. **Project Validation**:
   - Team can't benefit unless project reaches meaningful milestones
   - Aligns with product launch timelines
   - Demonstrates belief in long-term success

3. **Reduces Early Sell Pressure**:
   - Delays any team token sales until project is established
   - Community and ecosystem have time to mature
   - Token price can stabilize before insider sales begin

4. **Industry Standard**:
   - 1-year cliff is common in tech/crypto (borrowed from startup equity vesting)
   - Signals professional, serious project
   - Red flag if no cliff or very short cliff

**Smart Contract Implementation**:
Vesting is typically enforced on-chain via vesting contracts:
- Tokens allocated to vesting contract (not directly to recipients)
- Contract releases tokens based on timestamp
- Recipients can only withdraw vested amount
- Prevents circumventing vesting schedule

**Example Vesting Contract Logic**:
```solidity
contract TokenVesting {
    uint256 public cliff = 365 days;
    uint256 public vestingDuration = 4 * 365 days;
    uint256 public startTime;
    uint256 public totalAllocation;

    function vestedAmount() public view returns (uint256) {
        if (block.timestamp < startTime + cliff) {
            return 0; // Nothing vested during cliff
        }
        if (block.timestamp >= startTime + vestingDuration) {
            return totalAllocation; // Fully vested
        }
        // Linear vesting after cliff
        return totalAllocation * (block.timestamp - startTime) / vestingDuration;
    }
}
```

**Red Flags to Avoid**:
- No vesting for team/advisors (immediate dump risk)
- Very short vesting (< 1 year total)
- No cliff (tokens available immediately)
- Team allocation > 30% (insider control)
- Unequal vesting (team vests faster than community)

**Grading Criteria**:
- 13 points: Explains vesting, importance, typical schedule, and cliff purpose thoroughly
- 9-12 points: Good explanation but missing some details
- 6-8 points: Basic understanding but incomplete
- 3-5 points: Vague or superficial
- 0-2 points: Incorrect or no meaningful answer

---

## Answer Key Summary

| Question | Type | Answer | Points |
|----------|------|--------|--------|
| Q1 | MC | C | 8 |
| Q2 | MC | B | 8 |
| Q3 | MC | B | 8 |
| Q4 | MC | B | 8 |
| Q5 | MC | A | 8 |
| Q6 | MC | B | 8 |
| Q7 | SA | See model answer | 13 |
| Q8 | SA | See model answer | 13 |
| Q9 | SA | See model answer | 13 |
| Q10 | SA | See model answer | 13 |
| **Total** | | | **100** |

---

## Topics Covered

**Lectures L25-L32**:
- NFT real-world use cases (art, gaming, ticketing, credentials)
- NFT marketplaces and ecosystem
- Dynamic NFTs and metadata updates
- NFT royalties and EIP-2981
- NFT fractionalization
- Tokenomics fundamentals
- Token utility and value accrual
- Token distribution mechanisms (ICOs, airdrops, mining)
- Vesting schedules and cliffs
- Governance tokens and DAOs
- Supply models (circulating, total, max supply)
- Token burning and buybacks
- Incentive design

---

## Study Recommendations

- Review lecture slides L25-L32
- Study real-world NFT projects and their use cases
- Understand different token distribution models
- Know how vesting works and why it's important
- Study tokenomics of major projects (Uniswap, Aave, Compound)
- Understand governance mechanisms
- Review dynamic NFT implementations
- Explore NFT marketplace economics and royalty systems
