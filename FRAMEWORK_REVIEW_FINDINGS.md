# Munch-Engine Framework Review Findings
## Date: 2026-04-13

## Executive Summary
This review examines the Munch-Engine v2.0 framework documentation and implementation. The framework presents an innovative approach to AI agent operations through structured retrieval and knowledge persistence. However, significant inconsistencies exist between documented capabilities and actual implementation that undermine the framework's validity and practical utility.

## Key Findings

### 1. Critical Inconsistencies Between Documentation and Implementation

#### Broken Source References in Wiki
- **File:** `wiki/architecture/session-logic.md`
- **Claims:** References `src/auth/session.ts::validate#func` and `src/auth/session.ts::generateHash#func`
- **Reality:** These files do not exist in the repository
- **Actual Files Present:** Only `sample_app/src/core/auth.ts` and `sample_app/src/config.ts`
- **Impact:** The wiki contains non-functional references that break the savwiki → savref linkage

#### Missing Implementation Files for Examples
- **Playbook 01:** References `src/config/auth-constants.ts::JWT_EXPIRY#variable` - file does not exist
- **Playbook 02:** References Stripe documentation processing - no evidence of actual skill generation
- **Playbook 03:** References `global_sales_2025.csv` dataset - file does not exist
- **Playbook 2.0:** References `src/legacy-auth/session.ts::validate#func` - directory does not exist

### 2. Knowledge Persistence System Gaps

#### Wiki-Worker Skill Not Implemented
- **Documentation:** Claims wiki-Worker compiles Munch-Sync Signals into `/wiki`
- **Reality:** No automated wiki-update mechanism exists
- **Evidence:** Manual wiki pages exist but show no signs of programmatic updates from agent actions
- **Missing Component:** No tool or process for Wiki-Worker to consume Munch-Sync Signals

#### Munch-Sync Signal Mechanism Undefined
- **Documentation:** Tactical Workers emit Munch-Sync Signals upon task completion
- **Reality:** No standardized format or process for emitting/capturing these signals
- **Evidence:** Playbooks describe signals narratively but no machine-readable signal protocol exists

### 3. jMRI Loop Implementation Issues

#### Discovery Phase Misalignment
- **Documented Flow:** Director checks `/wiki` for savwiki before savref
- **Actual Behavior:** Examples show direct jumps to code search without wiki consultation
- **Example:** Playbook 01 searches for JWT_EXPIRY without first checking wiki

#### Context Hygiene Violations
- **Documented Principle:** Workers remain "blind" to broader repository
- **Actual Implementation:** No mechanism enforces context isolation for Tactical Workers
- **Evidence:** All examples show workers operating with full context awareness

### 4. Skills System Inconsistencies

#### Generated Skills Location Mismatch
- **Documentation:** Generated skills go to `/skills/generated/`
- **Reality:** Build-log.json indicates output to `/skills/core/` and `/wiki/skills/`
- **Conflict:** Creates confusion about where skills actually reside

#### Skill-Stripe Implementation Gap
- **Claim:** skill-stripe.md generated and saved to skills/generated/
- **Reality:** Only build-log.json exists; no actual skill file in expected location
- **Evidence:** build-log.json shows output_files pointing to skills/core/ and wiki/skills/

### 5. Framework Validity Assessment

#### Strengths
- Clear conceptual framework for AI agent operations
- Well-defined terminology (savwiki, savref, savraz, savtren)
- Structured approach to token efficiency through precision retrieval
- Comprehensive documentation of jMRI specification

#### Weaknesses
- **Implementation Gap:** Framework describes ideal state but lacks working implementation
- **Verification Deficit:** No evidence the described workflows actually function as documented
- **Dependency Issues:** Framework requires multiple MCP servers that may not be properly configured
- **Circular Dependencies:** Wiki depends on code that doesn't exist, code references wiki that doesn't contain accurate information

#### Reasonableness Evaluation
- **Conceptually Sound:** The theoretical framework addresses real AI agent limitations
- **Practically Unverified:** No working demonstration of the complete swarm system
- **Risk of Cargo Cult:** Teams may adopt terminology without functional underlying system

#### Potential for Positive User Outcomes
- **High Potential:** If implemented correctly, could significantly reduce token usage
- **Current Reality:** Framework functions more as aspirational documentation than working system
- **User Risk:** Teams investing time may find framework doesn't deliver promised benefits

## Actionable Suggestions

### Immediate Fixes (Priority: High)
1. **Resolve Reference Inconsistencies:**
   - Either create the missing source files referenced in wiki
   - OR update wiki references to point to actual existing files
   - Starting point: Align wiki/architecture/session-logic.md with sample_app/src/

2. **Implement Wiki-Worker Functionality:**
   - Create automated process for updating wiki from Munch-Sync Signals
   - Define standard signal format (JSON with insights, par~mi, savwiki updates)
   - Create wiki-update tool that consumes signals and modifies appropriate pages

3. **Fix Skills System:**
   - Clarify where generated skills should actually reside
   - Implement actual skill generation pipeline as described in Playbook 02
   - Ensure build-log.json accurately reflects actual outputs

### Medium-Term Improvements (Priority: Medium)
1. **Create Working Demonstrations:**
   - Implement at least one complete end-to-end example showing:
     - Director initialization from wiki
     - Tactical Worker execution with context hygiene
     - Wiki-Worker knowledge synthesis
     - Munch-Audit verification
   - Use the existing sample_app as the target substrate

2. **Enforce Context Hygiene:**
   - Implement mechanism to isolate Tactical Worker contexts
   - Create nok~ (near-context) enforcement tools
   - Add validation that workers only access assigned Stable IDs

3. **Standardize Munch-Sync Signals:**
   - Define JSON schema for signals
   - Create signal emission protocol for Tactical Workers
   - Build signal consumption pipeline for Wiki-Worker

### Long-Term Strategic Initiatives (Priority: Low)
1. **Framework Validation Suite:**
   - Create automated tests that verify framework claims
   - Build benchmark suite comparing framework to baseline approaches
   - Document actual token savings achieved

2. **User Onboarding Improvement:**
   - Create getting-started guide that works with actual implementation
   - Fix TUTORIAL.md to reference real files and working processes
   - Add verification steps users can perform to confirm framework operation

3. **Extension Ecosystem:**
   - Document how to create new skills that properly integrate with framework
   - Create skill template that enforces jMRI compliance
   - Build skill marketplace or registry

## Conclusion
The Munch-Engine v2.0 framework presents a compelling vision for structured AI agent operations with significant potential benefits in token efficiency and knowledge persistence. However, the current state reveals a substantial gap between documented ideals and actual implementation. The framework functions primarily as theoretical documentation rather than a working system.

To realize the framework's promised benefits, immediate attention must be given to resolving the fundamental inconsistencies between documentation and code. Without a working implementation that demonstrates the core jMRI Loop, Wiki-Worker synthesis, and context hygiene principles, the framework risks becoming an interesting but unusable conceptual exercise.

The path forward requires either scaling back the documentation to match actual capabilities or implementing the missing components to fulfill the framework's promises. Given the sophistication of the concepts presented, the latter approach would yield substantially greater value for users seeking to improve AI agent efficiency and knowledge persistence.