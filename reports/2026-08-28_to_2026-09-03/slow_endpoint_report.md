# Slow Endpoint Report: 2026-08-28 to 2026-09-03

Top 20 Slowest Queries
         • /getCrosstabResults – Latency : 3162 ms
         • /showRewardHistoryLog.do – Latency : 2041 ms
         • /addProfileCrosstabReport.do – Latency : 1204 ms
         • /getEngagementTrends – Latency : 1112 ms
         • /getAllActiveChildCommentsForComment – Latency : 733 ms
         • /reminderCount.do – Latency : 508 ms
         • /sendSurveyToFilteredMember – Latency : 497 ms
         • /getFilterMemberDetails – Latency : 449 ms
         • /redeemReward – Latency : 405 ms
         • /getActiveMembersTrend – Latency : 402 ms
         • /showMembers.do – Latency : 359 ms
         • /cacheInsightDataForInterval – Latency : 347 ms
         • /api/nativehtml/panel.reward.PanelRewardRedeem – Latency : 335 ms
         • /approveReward.do – Latency : 326 ms
         • /showCampaignBatch.do – Latency : 309 ms
         • /showPanelAdminSettings.do – Latency : 282 ms
         • /showPanelSegment.do – Latency : 275 ms
         • /showPanelProjectReminder.do – Latency : 266 ms
         • /showMemberRewardHistoryLog.do – Latency : 261 ms
         • /crossTab – Latency : 250 ms

---

## full breakdown (all endpoints seen across the week's top daily slots)

| endpoint | avg latency (ms) | total requests |
|---|---|---|
| `/a/ajs/survey-angular.panel.ProfileCrossTabAJSHandler-GetCrosstabResults` | 3162 | 24 |
| `/a/showRewardHistoryLog.do` | 2041 | 51 |
| `/a/addProfileCrosstabReport.do` | 1204 | 4 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetEngagementTrends` | 1112 | 1 |
| `/a/ajs/survey-angular.panel.portal.IdeaBoardAJSHandler-GetAllActiveChildCommentsForComment` | 733 | 3 |
| `/a/reminderCount.do` | 508 | 427 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-SendSurveyToFilteredMember` | 497 | 474 |
| `/a/ajs/survey-angular.panel.PanelDiscussionTopicAJSHandler-GetFilterMemberDetails` | 449 | 4 |
| `/a/ajs/survey-angular.panel.portal.PortalRewardAJSHandler-RedeemReward` | 405 | 81 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetActiveMembersTrend` | 402 | 1 |
| `/a/showMembers.do` | 359 | 354 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-CacheInsightDataForInterval` | 347 | 1 |
| `/a/api/nativehtml/panel.reward.PanelRewardRedeem` | 335 | 2 |
| `/a/approveReward.do` | 326 | 115 |
| `/a/showCampaignBatch.do` | 309 | 510 |
| `/a/showPanelAdminSettings.do` | 282 | 20 |
| `/a/showPanelSegment.do` | 275 | 2330 |
| `/a/showPanelProjectReminder.do` | 266 | 553 |
| `/a/showMemberRewardHistoryLog.do` | 261 | 4 |
| `/a/ajs/cx-angular.cx.dashboard.SurveyDashboardAPI-CrossTab` | 250 | 4 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-GetPanelFilter` | 231 | 866 |
| `/a/searchMember.do` | 223 | 1412 |
| `/a/uploadNewPanelDocument.do` | 217 | 11 |
| `/a/searchCampaignBatchProject.do` | 179 | 71 |
| `/a/showPanelDocuments.do` | 168 | 3 |
| `/a/deleteQPointInventoryItem.do` | 160 | 6 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-GetPanelMemberFilterDeliveryOption` | 159 | 2 |
| `/a/showQPointInventoryItems.do` | 155 | 13 |
| `/a/showPanelReport.do` | 144 | 18 |
| `/a/ShareCrosstab` | 130 | 40 |
| `/a/ajs/survey-angular.panel.portal.PanelMemberAccountAJSHandler-GetLeaderBoard` | 125 | 1391 |
| `/a/ajs/survey-angular.panel.portal.PortalDashBoardAJSHandler-GetDiscussionDetails` | 111 | 15 |
| `/a/copyBroadcast.do` | 108 | 4 |
| `/a/showOrgUsersPanel.do` | 103 | 7 |
| `/a/newPanelWizardName.do` | 101 | 157 |
| `/a/deletePanelMember.do` | 101 | 1 |
| `/a/searchSurveyCampaignBatch.do` | 100 | 1077 |
| `/a/ajs/survey-angular.panel.analytics.panelretail.ajs.iron.PanelRetailDashboardAJSHandler-GetBasketMetrics` | 95 | 2 |
| `/a/saveMemberQPoints.do` | 95 | 13 |
| `/a/ajs/survey-angular.panel.profile.ajs.iron.PanelProfileAJSHandler-ImportProfileFields` | 89 | 16 |
| `/a/showQPointIncentive.do` | 86 | 126 |
| `/a/ajs/survey-angular.panel.portal.PortalDashBoardAJSHandler-GetTopicDetails` | 84 | 16 |
| `/a/showDiscussionModule.do` | 84 | 110 |
| `/a/showPanelUserReport.do` | 81 | 366 |
| `/a/ajs/survey-angular.panel.analytics.panelretail.ajs.iron.PanelRetailDashboardAJSHandler-GetSpendOverTime` | 77 | 1 |
| `/a/showPanelRecruitmentSetting.do` | 70 | 68 |
| `/a//showQPointInventoryItems.do` | 69 | 17 |
| `/a/showPanelMemberDashBoard.do` | 69 | 949 |
| `/a/ajs/survey-angular.panel.portal.PanelMemberAccountAJSHandler-UpdateMemberDetailsFromAccount` | 58 | 5 |
| `/a/showPanelAdvanceSettings.do` | 56 | 13 |
| `/a/addQPointInventoryItems.do` | 55 | 14 |
| `/a/showProfileCrossTabReport.do` | 54 | 4 |
| `/a/deleteBulkBroadcast.do` | 53 | 1 |
| `/a/ajs/survey-angular.panel.portal.PortalRewardAJSHandler-GetAllAvailableRewards` | 52 | 318 |
| `/a/ajs/survey-angular.panel.portal.DiscussionTopicAJSHandler-AddUpdateComment` | 46 | 1 |
| `/a/showPanelLandingDashboard.do` | 41 | 37 |
| `/a/router.do` | 40 | 3 |
| `/a/api/nativehtml/panel.member.PanelMemberProfileFields` | 40 | 3 |
| `/a/ajs/survey-angular.panel.portal.PortalDashBoardAJSHandler-GetSurveyDetails` | 38 | 728 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-GetPanelMemberFilterCount` | 37 | 232 |
| `/a/savePanelAdvanceSettings.do` | 36 | 7 |
| `/a/ajs/survey-angular.panel.portal.IdeaBoardAJSHandler-AddIdea` | 30 | 4 |
| `/a/ajs/survey-angular.panel.portal.IdeaBoardAJSHandler-AddUpdateComment` | 29 | 3 |

---

## Copy-paste block

```
Top 20 Slowest Queries
         • /getCrosstabResults – Latency : 3162 ms
         • /showRewardHistoryLog.do – Latency : 2041 ms
         • /addProfileCrosstabReport.do – Latency : 1204 ms
         • /getEngagementTrends – Latency : 1112 ms
         • /getAllActiveChildCommentsForComment – Latency : 733 ms
         • /reminderCount.do – Latency : 508 ms
         • /sendSurveyToFilteredMember – Latency : 497 ms
         • /getFilterMemberDetails – Latency : 449 ms
         • /redeemReward – Latency : 405 ms
         • /getActiveMembersTrend – Latency : 402 ms
         • /showMembers.do – Latency : 359 ms
         • /cacheInsightDataForInterval – Latency : 347 ms
         • /api/nativehtml/panel.reward.PanelRewardRedeem – Latency : 335 ms
         • /approveReward.do – Latency : 326 ms
         • /showCampaignBatch.do – Latency : 309 ms
         • /showPanelAdminSettings.do – Latency : 282 ms
         • /showPanelSegment.do – Latency : 275 ms
         • /showPanelProjectReminder.do – Latency : 266 ms
         • /showMemberRewardHistoryLog.do – Latency : 261 ms
         • /crossTab – Latency : 250 ms
```