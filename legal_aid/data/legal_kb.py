# Pakistani Legal Knowledge Base
# This file contains summarized Pakistani laws for RAG

LEGAL_KNOWLEDGE = [
    {
        "id": "labor_001",
        "category": "Labor Law",
        "title": "Employment / Wrongful Termination",
        "content": """
Under Pakistani labor law, the Industrial and Commercial Employment (Standing Orders) Ordinance 1968 
governs employment relationships. An employee cannot be terminated without:
1. A valid written reason
2. One month's notice or one month's salary in lieu of notice
3. Due process including a show cause notice and opportunity to be heard

Wrongful termination entitles the employee to:
- Reinstatement with back pay, OR
- Compensation equivalent to 30 days wages for each year of service
- Gratuity payment if employed for more than one year

Relevant courts: Labor Court under Industrial Relations Act 2012
Complaint procedure: File complaint with Labor Commissioner within 3 months of termination
        """,
        "keywords": ["fired", "terminated", "job loss", "dismissal", "employment", "workplace", "salary", "wages", "ملازمت", "نوکری"]
    },
    {
        "id": "consumer_001",
        "category": "Consumer Protection",
        "title": "Consumer Rights / Fraud / Defective Products",
        "content": """
The Consumer Protection Act exists in all four provinces of Pakistan:
- Punjab Consumer Protection Act 2005
- Sindh Consumer Protection Act 2014
- KPK Consumer Protection Act 1997
- Balochistan Consumer Protection Act 2003

Consumer rights include:
1. Right to safety from hazardous goods/services
2. Right to information about quality, quantity, potency, purity
3. Right to be heard and seek redressal
4. Right to compensation for defective goods or deficient services

Remedies available:
- Replacement of defective product
- Full refund
- Compensation for loss/injury
- Penalty on seller up to Rs. 100,000

Filing procedure: File written complaint with District Consumer Court
Time limit: Within 30 days of cause of action
        """,
        "keywords": ["fraud", "scam", "defective product", "refund", "consumer", "cheated", "fake", "دھوکہ", "مال"]
    },
    {
        "id": "property_001",
        "category": "Property Law",
        "title": "Property Disputes / Illegal Possession / Rent",
        "content": """
Key property laws in Pakistan:
- Transfer of Property Act 1882
- Rent Restriction Acts (provincial)
- Land Revenue Act 1967

For illegal possession (Qabza):
- File FIR under Section 447 PPC (criminal trespass)
- File civil suit for possession under CPC Order 39
- Apply for injunction in Civil Court

For rent disputes:
- Rent Controller has jurisdiction over tenancy matters
- Landlord cannot evict without court order
- Tenant has right to receipt for every payment
- 30 days notice required before rent increase

For property fraud:
- File complaint under Section 420 PPC (cheating) and 468 PPC (forgery)
- Report to FIA Cybercrime if online fraud
- File civil suit for declaration of title

Court: Civil Court → High Court (appeal)
        """,
        "keywords": ["property", "land", "house", "rent", "eviction", "possession", "qabza", "tenant", "landlord", "مکان", "زمین", "جائیداد", "کرایہ"]
    },
    {
        "id": "family_001",
        "category": "Family Law",
        "title": "Divorce / Khula / Maintenance / Child Custody",
        "content": """
Muslim Family Laws Ordinance 1961 governs family matters in Pakistan.

DIVORCE (Talaq):
- Husband must send written notice to Union Council
- 90-day reconciliation period mandatory
- Divorce effective after 90 days if no reconciliation

KHULA (Woman's right to divorce):
- Woman can seek Khula through Family Court
- Must return Haq Mehr (dower) to husband
- Family Court can grant Khula if reconciliation fails

MAINTENANCE (Nafqah):
- Husband legally obligated to maintain wife and children
- Court can order maintenance if husband refuses
- File application in Family Court

CHILD CUSTODY:
- Mother gets custody of sons until age 7
- Mother gets custody of daughters until puberty
- Father is natural guardian for property matters
- Child's welfare is paramount consideration

Court: Family Court under Family Courts Act 1964
        """,
        "keywords": ["divorce", "khula", "talaq", "maintenance", "custody", "marriage", "husband", "wife", "child", "طلاق", "خلع", "نفقہ", "بچے"]
    },
    {
        "id": "cyber_001",
        "category": "Cyber Crime",
        "title": "Online Fraud / Harassment / Data Theft",
        "content": """
Prevention of Electronic Crimes Act (PECA) 2016 governs cyber crimes in Pakistan.

ONLINE FRAUD:
- Section 14: Unauthorized access to data - up to 3 months imprisonment
- Section 16: Electronic fraud - up to 2 years imprisonment + fine

CYBER HARASSMENT:
- Section 20: Offenses against dignity - up to 3 years + Rs. 1 million fine
- Section 21: Cyber stalking - up to 3 years + Rs. 1 million fine

FAKE SOCIAL MEDIA PROFILES / MORPHED IMAGES:
- Section 20 PECA applies - up to 3 years imprisonment

HOW TO REPORT:
1. File complaint at FIA Cybercrime Wing: complaint.fia.gov.pk
2. Call FIA helpline: 1787
3. Visit nearest FIA Cybercrime Circle office
4. Preserve all digital evidence (screenshots, URLs)

FIA offices in: Karachi, Lahore, Islamabad, Peshawar, Quetta
        """,
        "keywords": ["online fraud", "hacking", "harassment", "social media", "fake account", "blackmail", "cyber", "internet", "FIA", "آن لائن", "سائبر"]
    },
    {
        "id": "criminal_001",
        "category": "Criminal Law",
        "title": "FIR / Police Complaints / Bail",
        "content": """
Pakistan Penal Code 1860 and Code of Criminal Procedure 1898 govern criminal matters.

FILING FIR:
- FIR (First Information Report) is right of every citizen
- Police cannot refuse to register FIR for cognizable offenses
- If police refuse: Approach DSP/SSP or Magistrate under Section 22-A CrPC
- FIR must be read back to complainant before signing

TYPES OF OFFENSES:
- Cognizable: Police can arrest without warrant (murder, robbery, kidnapping)
- Non-cognizable: Police need warrant (minor offenses)

BAIL:
- Bailable offenses: Police must grant bail upon request
- Non-bailable: Only court can grant bail
- Pre-arrest bail: Apply to High Court under Section 498 CrPC
- Post-arrest bail: Apply to Sessions Court

IMPORTANT SECTIONS:
- 302 PPC: Murder
- 307 PPC: Attempted murder
- 406 PPC: Criminal breach of trust
- 420 PPC: Cheating/fraud
- 506 PPC: Criminal intimidation/threatening
        """,
        "keywords": ["FIR", "police", "arrest", "bail", "criminal", "complaint", "theft", "robbery", "murder", "threatening", "ایف آئی آر", "پولیس", "ضمانت"]
    },
    {
        "id": "banking_001",
        "category": "Banking & Finance",
        "title": "Bank Fraud / Loan Issues / Insurance",
        "content": """
State Bank of Pakistan (SBP) regulates banking sector.

BANKING FRAUD:
- Report immediately to your bank's fraud department
- Contact SBP Banking Mohtasib: 0800-00008 (toll-free)
- File complaint at: bankingmohtasib.gov.pk
- FIA Cybercrime for online banking fraud

UNAUTHORIZED TRANSACTIONS:
- Bank must reverse unauthorized transactions within 10 working days
- Bank has liability if fraud occurs due to bank's negligence

LOAN HARASSMENT:
- Banks cannot use threatening tactics for loan recovery
- File complaint with SBP if bank agents harass you
- Consumer Protection Tribunal has jurisdiction

INSURANCE DISPUTES:
- Regulated by Securities and Exchange Commission of Pakistan (SECP)
- File complaint at: eservices.secp.gov.pk
- Insurance Ombudsman for unresolved disputes

Relevant laws: Banking Companies Ordinance 1962, Financial Institutions Ordinance 2001
        """,
        "keywords": ["bank", "loan", "fraud", "account", "insurance", "ATM", "transaction", "بینک", "قرض", "انشورنس"]
    }
]
