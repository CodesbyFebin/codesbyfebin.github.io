"""Visible direct answers and editorial cross-links used by the static builder."""
ANSWERS = {
 'home':('What does CodesbyFebin build?','Febin Francis focuses on AI infrastructure, verifiable compute, and sovereign self-hosted systems. This portfolio connects project source code with engineering notes and technical references.'),
 'about':('Where is Febin Francis based?','Febin Francis is based in Kerala, India, in the Indian Standard Time zone, UTC+5:30. Public identity links are provided for GitHub, LinkedIn, and ORCID.'),
 'systems':('Where can I inspect the systems architecture?','The systems page includes architecture discussion and labeled repository documentation snapshots. Project guides link to the current repositories; the specifications page provides source-linked contracts and threat-model references.'),
 'projects':('How can I find a repository?','Browse the populated directory of 23 repositories. With JavaScript enabled, combine text search, category and review-status filters, then sort by name, dated stars, or source-update date. All repositories remain visible without JavaScript.'),
 'blog':('Are these engineering notes published research papers?','These are engineering notes provided directly on this website. Research interests and external identity links are presented separately on the research page; the site does not claim an unverified publication record.'),
 'services':('How do I propose a technical collaboration?','Describe the current system, source repository, desired result, constraints, and acceptance evidence. Use the contact page to prepare a local brief and the public GitHub or LinkedIn profile to start the conversation.'),
 'research':('Where is the research identity profile?','The linked ORCID profile is 0009-0002-8123-1531. This page describes research interests and possible questions to test; it does not invent papers, citation counts, or academic affiliations.'),
 'contributions':('How can I contribute to a CodesbyFebin project?','Open the relevant repository, read its current contribution instructions, and propose a reproducible issue or focused patch. Include the environment, expected behavior, observed behavior, and a check that demonstrates the correction.'),
 'contact':('Does the contact form send a message?','The brief builder formats text locally on your device. It does not submit a message. Copy the prepared brief and use the linked GitHub or LinkedIn profile to contact Febin Francis.'),
 'specifications':('Are the technical references independent test results?','No. Repository documentation snapshots are labeled with their source and review date. They describe contracts, scope, and testing approaches; they are not fresh runtime test reports or proof of production deployment.')}
RELATED = {
 'home':['about','systems','projects','blog','services'],
 'about':['systems','projects','research','contact'],
 'systems':['projects','specifications','blog','research'],
 'projects':['systems','blog','contributions','specifications'],
 'blog':['systems','projects','research','specifications'],
 'services':['systems','specifications','contributions','contact'],
 'research':['systems','blog','specifications','contributions'],
 'contributions':['projects','specifications','blog','contact'],
 'contact':['services','projects','about','contributions'],
 'specifications':['systems','projects','research','contributions']}
LABELS={'home':'Portfolio home','about':'Systems engineer in Kerala, India','systems':'Verifiable compute and self-hosted systems','projects':'Open-source repository directory','blog':'AI infrastructure engineering notes','services':'Systems architecture collaboration','research':'Verifiable compute research interests','contributions':'Open-source contribution workflow','contact':'Technical collaboration contact','specifications':'Protocol and evidence specifications'}
