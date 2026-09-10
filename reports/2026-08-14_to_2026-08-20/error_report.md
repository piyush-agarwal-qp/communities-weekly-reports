# weekly error report — 2026-08-14 to 2026-08-20

**date range:** 2026-08-14 → 2026-08-20
**total errors:** 78
**clusters:** 20

---

## summary table

| # | sev | root cause | count | dc | side | dates |
|---|-----|-----------|-------|-----|------|-------|
| 1 | high | java.util.ConcurrentModificationException | 34 | EU | portal | 2026-08-15 → 2026-08-19 |
| 2 | medium | java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micropanel.Pane | 8 | EU | other | 2026-08-14 |
| 3 | low | Root Exception :
org.apache.xmlrpc.XmlRpcException: Failed to create input strea | 2 | EU | other | 2026-08-19 |
| 4 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 5 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 6 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 7 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 8 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 9 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 10 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 11 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 12 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 13 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 14 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 15 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 16 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 17 | low | Root Exception : | 2 | US | other | 2026-08-18 |
| 18 | low | java.lang.IndexOutOfBoundsException: Index 0 out of bounds for length 0 | 2 | US | other | 2026-08-18 |
| 19 | low | UserPreparedStatement[SpyPreparedStatement[null]] | 2 | QA | panel | 2026-08-17 |
| 20 | low | com.surveyconsole.batch.error.ProcessingItemRejectedException: Rejected! Another | 2 | EU | other | 2026-08-15 |

---

## dc & side breakdown

| dc | portal | panel | other |
|----|--------|-------|-------|
| us | 0 | 0 | 15 |
| eu | 1 | 0 | 3 |
| qa | 0 | 1 | 0 |

---

## cluster details

### 1. java.util.ConcurrentModificationException *(high, 34 hits)*

**dc / side:** eu · portal
**endpoint:** `survey-angular.panel.portal.PortalSurveyAJSHandler-GetAllSurveys`
**dates:** 2026-08-15 → 2026-08-19
**affected hosts:** pveuqprun2.questionpro.net, pveuqprun3.questionpro.net, pveuqprun4.questionpro.net
**error ids (sample 5/34):** 2462591, 2461821, 2460287, 2459949, 2457493

**request context:**

- referer: `https://onepolluk.questionpro.eu/a/showMemberSurveys.do?lppn=false`

**root cause:**
```
java.util.ConcurrentModificationException
```

**codebase frames:**
```
at com.surveyconsole.angular.panel.portal.PanelLogSurveyFetcher.getCachedSurveyIds(PanelLogSurveyFetcher.java:48)
at com.surveyconsole.angular.panel.portal.PanelLogSurveyFetcher.getMemberSurveyIdsFromPanelLog(PanelLogSurveyFetcher.java:56)
at com.surveyconsole.angular.panel.portal.PanelMemberSurveyFetcher.updateCachedSurveysOfPanelLog(PanelMemberSurveyFetcher.java:81)
at com.surveyconsole.angular.panel.portal.PanelMemberSurveyFetcher.getPanelMemberSurveysObject(PanelMemberSurveyFetcher.java:94)
at com.surveyconsole.angular.panel.portal.PortalSurveyAJSHandler.apiGetAllSurveys(PortalSurveyAJSHandler.java:25)
```

---

### 2. java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micro *(medium, 8 hits)*

**dc / side:** eu · other
**endpoint:** `/a/showLiveDiscussions.do`
**dates:** 2026-08-14
**affected hosts:** pveuadminapp1.questionpro.net
**error ids (sample 5/8):** 2414309, 2414308, 2414307, 2414306, 2414309

**request context:**

- referer: `https://euadmin.questionpro.com/a/showLiveDiscussions.do?lppn=false`

**root cause:**
```
java.lang.NullPointerException: Cannot invoke "com.surveyconsole.micropanel.PanelMember.getSelectedLanguage()" because "member" is null
```

**codebase frames:**
```
at com.surveyconsole.micropanel.polls.PanelPollUtil.getNewPollForm(PanelPollUtil.java:73)
at com.surveyconsole.micropanel.PanelMember.getPanelPollHTML(PanelMember.java:11733)
at com.surveyconsole.micropanel.PanelPollManager.getUserPollHTMLNew(PanelPollManager.java:528)
at com.surveyconsole.application.logs.filter.MDCFilter.filter(MDCFilter.java:26)
at com.bhaskaran.application.filter.FilterAdapter.doFilter(FilterAdapter.java:14)
at com.surveyconsole.intercom.IntercomAppFilter.filter(IntercomAppFilter.java:28)
```

---

### 3. Root Exception :
org.apache.xmlrpc.XmlRpcException: Failed to create i *(low, 2 hits)*

**dc / side:** eu · other
**endpoint:** `(unknown)`
**dates:** 2026-08-19
**affected hosts:** pveuqprun3.questionpro.net
**error ids (sample 2/2):** 2455889, 2455889

**root cause:**
```
Root Exception :
org.apache.xmlrpc.XmlRpcException: Failed to create input stream: Server returned HTTP response code: 502 for URL: http://eu-data.questionpro.net/a/xmlrpc
	at org.apache.xmlrpc.client
```

**codebase frames:**
```
at com.surveyconsole.batch.KickStartServices.getSurveyResponseCountByDataSource(KickStartServices.java:325)
at com.surveyconsole.builder.ListSurveysAction$1.runLogged(ListSurveysAction.java:370)
at com.bhaskaran.processor.ErrorLoggedThread.run(ErrorLoggedThread.java:66)
at com.surveyconsole.batch.KickStartServices.getSurveyResponseCountByDataSource(KickStartServices.java:328)
at com.surveyconsole.builder.ListSurveysAction$1.runLogged(ListSurveysAction.java:370)
at com.bhaskaran.processor.ErrorLoggedThread.run(ErrorLoggedThread.java:66)
```

---

### 4. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449771, 2449771

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.html.MULTICHOICEDisplay.printVertical(MULTICHOICEDisplay.java:445)
at com.surveyconsole.html.MULTICHOICEDisplay.display(MULTICHOICEDisplay.java:96)
at com.surveyconsole.html.Display.externalDisplay(Display.java:72)
at com.surveyconsole.infra.Section.toHTML(Section.java:201)
```

---

### 5. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449770, 2449770

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.infra.Answer.getInlineLogicControl(Answer.java:970)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:329)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:300)
at com.surveyconsole.html.UNICHOICEDisplay.printVertical(UNICHOICEDisplay.java:713)
```

---

### 6. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449769, 2449769

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.infra.Answer.getInlineLogicControl(Answer.java:970)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:329)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:300)
at com.surveyconsole.html.UNICHOICEDisplay.printVertical(UNICHOICEDisplay.java:713)
```

---

### 7. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449768, 2449768

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.infra.Answer.getInlineLogicControl(Answer.java:970)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:329)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:300)
at com.surveyconsole.html.UNICHOICEDisplay.printVertical(UNICHOICEDisplay.java:713)
```

---

### 8. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449767, 2449767

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.infra.Answer.getInlineLogicControl(Answer.java:970)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:329)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:300)
at com.surveyconsole.html.UNICHOICEDisplay.printVertical(UNICHOICEDisplay.java:713)
```

---

### 9. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449766, 2449766

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.infra.Answer.getInlineLogicControl(Answer.java:970)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:329)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:300)
at com.surveyconsole.html.UNICHOICEDisplay.printVertical(UNICHOICEDisplay.java:713)
```

---

### 10. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449765, 2449765

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.infra.Answer.getInlineLogicControl(Answer.java:970)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:329)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:300)
at com.surveyconsole.html.UNICHOICEDisplay.printVertical(UNICHOICEDisplay.java:713)
```

---

### 11. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449764, 2449764

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.infra.Answer.getInlineLogicControl(Answer.java:970)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:329)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:300)
at com.surveyconsole.html.UNICHOICEDisplay.printVertical(UNICHOICEDisplay.java:713)
```

---

### 12. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449763, 2449763

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.infra.Answer.getInlineLogicControl(Answer.java:970)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:329)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:300)
at com.surveyconsole.html.UNICHOICEDisplay.printVertical(UNICHOICEDisplay.java:713)
```

---

### 13. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449762, 2449762

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.html.MULTICHOICEDisplay.printVertical(MULTICHOICEDisplay.java:445)
at com.surveyconsole.html.MULTICHOICEDisplay.display(MULTICHOICEDisplay.java:96)
at com.surveyconsole.html.Display.externalDisplay(Display.java:72)
at com.surveyconsole.infra.Section.toHTML(Section.java:201)
```

---

### 14. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449761, 2449761

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.html.MULTICHOICEDisplay.printVertical(MULTICHOICEDisplay.java:445)
at com.surveyconsole.html.MULTICHOICEDisplay.display(MULTICHOICEDisplay.java:96)
at com.surveyconsole.html.Display.externalDisplay(Display.java:72)
at com.surveyconsole.infra.Section.toHTML(Section.java:201)
```

---

### 15. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449760, 2449760

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.infra.Answer.getInlineLogicControl(Answer.java:970)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:329)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:300)
at com.surveyconsole.html.UNICHOICEDisplay.printVertical(UNICHOICEDisplay.java:713)
```

---

### 16. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449759, 2449759

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.html.MULTICHOICEDisplay.printVertical(MULTICHOICEDisplay.java:445)
at com.surveyconsole.html.MULTICHOICEDisplay.display(MULTICHOICEDisplay.java:96)
at com.surveyconsole.html.Display.externalDisplay(Display.java:72)
at com.surveyconsole.infra.Section.toHTML(Section.java:201)
```

---

### 17. Root Exception : *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `(unknown)`
**dates:** 2026-08-18
**affected hosts:** pvqpadminapp2.questionpro.net
**error ids (sample 2/2):** 2449758, 2449758

**request context:**

- referer: `null`

**root cause:**
```
Root Exception :
```

**codebase frames:**
```
at com.surveyconsole.infra.QuestionListManager.getQuestion(QuestionListManager.java:436)
at com.surveyconsole.infra.Survey.getQuestion(Survey.java:2067)
at com.surveyconsole.infra.Answer.getInlineLogicControl(Answer.java:970)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:329)
at com.surveyconsole.html.SectionDisplay.getAnswerText(SectionDisplay.java:300)
at com.surveyconsole.html.UNICHOICEDisplay.printVertical(UNICHOICEDisplay.java:713)
```

---

### 18. java.lang.IndexOutOfBoundsException: Index 0 out of bounds for length  *(low, 2 hits)*

**dc / side:** us · other
**endpoint:** `/a/loadResponse.do`
**dates:** 2026-08-18
**affected hosts:** qpweb3.questionpro.net
**error ids (sample 2/2):** 2449131, 2449131

**request context:**

- referer: `https://www.questionpro.com/a/frame.do?mode=viewIndividual&surveyID=EIMBWKGqMBqLkPMt32mMiSo02pSR_vzStQ.MqLnTIrM-&responseSetID=mhvKfSIw92_NVcm46CpNibAuJ8qBPogLGc_RIVrHzQk-`
- params: `surveyID=13323446&responseSetID=150462045`

**root cause:**
```
java.lang.IndexOutOfBoundsException: Index 0 out of bounds for length 0
```

**codebase frames:**
```
at com.surveyconsole.html.TEXTLoader.loadInternal(TEXTLoader.java:44)
at com.surveyconsole.html.Loader.load(Loader.java:36)
at com.surveyconsole.analysis.ResponseLoader.loadData(ResponseLoader.java:832)
at com.surveyconsole.analysis.ResponseLoader.loadSectionResponse(ResponseLoader.java:776)
at com.surveyconsole.analysis.ResponseLoader.load(ResponseLoader.java:718)
at com.surveyconsole.analysis.ResponseLoader.load(ResponseLoader.java:695)
```

---

### 19. UserPreparedStatement[SpyPreparedStatement[null]] *(low, 2 hits)*

**dc / side:** qa · panel
**endpoint:** `/a/inviteUsers.do`
**dates:** 2026-08-17
**affected hosts:** qa1.du
**error ids (sample 2/2):** 2440335, 2440335

**request context:**

- referer: `https://aeqa.questionpro.com/a/showPanelUserReport.do?lcfpn=false`
- params: `ajax=true&engine=dojo&text=selenium-communities+test+ae@questionpro.com,TestTest123,7894561239,TestA,TestB,TestC,Selenium@123&info=-1`

**root cause:**
```
UserPreparedStatement[SpyPreparedStatement[null]]
```

**codebase frames:**
```
at com.bhaskaran.database.PreparedInsertCommand.executeWithConnection(PreparedInsertCommand.java:39)
at com.bhaskaran.database.ConnectionCommand.execute(ConnectionCommand.java:66)
at com.bhaskaran.database.PreparedInsertCommand.execute(PreparedInsertCommand.java:123)
at com.surveyconsole.micropanel.BulkInsertPanelMemberProcessor.executeMultiplePanelMemberInsert(BulkInsertPanelMemberProcessor.java:161)
at com.surveyconsole.micropanel.BulkInsertPanelMemberProcessor.bulkInsertPanelMembers(BulkInsertPanelMemberProcessor.java:88)
at com.surveyconsole.micropanel.PanelMemberImportHandler.createOrUpdatePanelMember(PanelMemberImportHandler.java:34)
```

---

### 20. com.surveyconsole.batch.error.ProcessingItemRejectedException: Rejecte *(low, 2 hits)*

**dc / side:** eu · other
**endpoint:** `(unknown)`
**dates:** 2026-08-15
**affected hosts:** pveuqpweb1.questionpro.net
**error ids (sample 2/2):** 2422076, 2422076

**root cause:**
```
com.surveyconsole.batch.error.ProcessingItemRejectedException: Rejected! Another process already in progress
```

**codebase frames:**
```
at com.surveyconsole.batch.LongProcessHandler.startProcessingForCommunities(LongProcessHandler.java:101)
at com.surveyconsole.micropanel.broadcast.SendBroadcastHandler.processBroadcastNotification(SendBroadcastHandler.java:39)
at com.surveyconsole.micropanel.broadcast.SendBroadcastHandler.sendBroadcastNotification(SendBroadcastHandler.java:30)
at com.surveyconsole.micropanel.analysis.SendBroadcastNotificationAction.doPerformBroadcast(SendBroadcastNotificationAction.java:63)
at com.surveyconsole.micropanel.PanelBroadcastEmailAction.doPerform(PanelBroadcastEmailAction.java:44)
at com.bhaskaran.ui.ActionAdapter.lambda$perform$0(ActionAdapter.java:299)
```

---

## pdm report

```
78 errors logged (2026-08-14 → 2026-08-20)

us dc — 0 panel, 0 portal
eu dc — 0 panel, 1 portal
qa    — 1 panel, 0 portal  (non-production)
```

---

## engineering update

```
78 errors | panel-0, portal-0 (us) | panel-0, portal-1 (eu)

~ 34  : [2026-08-15→2026-08-19] java.util.concurrentmodificationexception — survey-angular.panel.portal.PortalSurveyAJSHandler-GetAllSurveys
~ 8   : [2026-08-14] java.lang.nullpointerexception: cannot invoke "com.surveyconsole.micropanel.panelmember.getselectedl — /a/showLiveDiscussions.do
```