# Slow Endpoint Report: 2026-08-21 to 2026-08-27

Top 20 Slowest Queries
         • /getSurveyAbandonedMembers – Latency : 8758 ms
         • /getCrosstabResults – Latency : 2409 ms
         • /reminderCount.do – Latency : 960 ms
         • /sendSurveyToFilteredMember – Latency : 653 ms
         • /showPanelAdminSettings.do – Latency : 640 ms
         • /showPanelProjectReminder.do – Latency : 406 ms
         • /getAtRiskMembers – Latency : 388 ms
         • /approveReward.do – Latency : 380 ms
         • /redeemReward – Latency : 323 ms
         • /showMembers.do – Latency : 306 ms
         • /api/nativehtml/panel.reward.PanelRewardRedeem – Latency : 294 ms
         • /getPanelFilter – Latency : 269 ms
         • /searchMember.do – Latency : 258 ms
         • /updateFilteredMemberStatus – Latency : 258 ms
         • /ShareCrosstab – Latency : 256 ms
         • /newPanelWizardName.do – Latency : 253 ms
         • /showRewardResolvedLog.do – Latency : 248 ms
         • /showRewardHistoryLog.do – Latency : 236 ms
         • /getActiveMembersTrend – Latency : 233 ms
         • /getEngagementTrends – Latency : 228 ms

---

## full breakdown (all endpoints seen across the week's top daily slots)

| endpoint | avg latency (ms) | total requests |
|---|---|---|
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetSurveyAbandonedMembers` | 8758 | 1 |
| `/a/ajs/survey-angular.panel.ProfileCrossTabAJSHandler-GetCrosstabResults` | 2409 | 16 |
| `/a/reminderCount.do` | 960 | 550 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-SendSurveyToFilteredMember` | 653 | 409 |
| `/a/showPanelAdminSettings.do` | 640 | 2 |
| `/a/showPanelProjectReminder.do` | 406 | 928 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetAtRiskMembers` | 388 | 1 |
| `/a/approveReward.do` | 380 | 191 |
| `/a/ajs/survey-angular.panel.portal.PortalRewardAJSHandler-RedeemReward` | 323 | 130 |
| `/a/showMembers.do` | 306 | 633 |
| `/a/api/nativehtml/panel.reward.PanelRewardRedeem` | 294 | 8 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-GetPanelFilter` | 269 | 981 |
| `/a/searchMember.do` | 258 | 1258 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-UpdateFilteredMemberStatus` | 258 | 13 |
| `/a/ShareCrosstab` | 256 | 74 |
| `/a/newPanelWizardName.do` | 253 | 174 |
| `/a/showRewardResolvedLog.do` | 248 | 11 |
| `/a/showRewardHistoryLog.do` | 236 | 5 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetActiveMembersTrend` | 233 | 1 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetEngagementTrends` | 228 | 1 |
| `/a/showPanelSegment.do` | 198 | 2168 |
| `/a/showCampaignBatch.do` | 197 | 707 |
| `/a/searchCampaignBatchProject.do` | 171 | 130 |
| `/a/searchSurveyCampaignBatch.do` | 147 | 2197 |
| `/a/ajs/survey-angular.panel.portal.PanelMemberAccountAJSHandler-GetLeaderBoard` | 135 | 2279 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-GetPanelMemberFilterDeliveryOption` | 134 | 9 |
| `/a/showQPointIncentive.do` | 131 | 123 |
| `/a/showPanelFTPExportSchedulerEvents.do` | 115 | 19 |
| `/a/showPanelReport.do` | 115 | 6 |
| `/a/bulkDeleteMembers.do` | 112 | 1 |
| `/a/ajs/survey-angular.panel.portal.PortalDashBoardAJSHandler-GetDiscussionDetails` | 111 | 10 |
| `/a/panelMemberFilterSearch.do` | 109 | 7 |
| `/a/showLiveDiscussions.do` | 108 | 2 |
| `/a/ajs/survey-angular.panel.PanelDiscussionTopicAJSHandler-GetFilterMemberDetails` | 100 | 12 |
| `/a/ajs/survey-angular.panel.PanelFilterAJSHandler-GetPanelMemberFilterCount` | 99 | 130 |
| `/a/ajs/survey-angular.panel.modules.polls.iron.PanelPollAJSHandler-GetPanelPollByID` | 95 | 1 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-CacheInsightDataForInterval` | 93 | 4 |
| `/a/ajs/survey-angular.panel.profile.ajs.iron.PanelProfileAJSHandler-ImportProfileFields` | 90 | 16 |
| `/a/deletePanelMember.do` | 90 | 1 |
| `/a/api/nativehtml/panel.idea.IdeaComments` | 89 | 1 |
| `/a/api/nativehtml/panel.idea.AddUpdateIdeaVote` | 89 | 1 |
| `/a/newPanelWizardLandingPage.do` | 84 | 38 |
| `/a/ajs/survey-angular.panel.portal.IdeaBoardAJSHandler-AddIdea` | 80 | 7 |
| `/a/showOrgUsersPanel.do` | 80 | 12 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetEngagementDrivers` | 78 | 1 |
| `/a/showPanelLandingDashboard.do` | 73 | 14 |
| `/a/showProfileCrossTabReport.do` | 68 | 2 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetTopEngagedMembers` | 64 | 1 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetActivityTrends` | 58 | 1 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetMembersActivityHeatmap` | 57 | 1 |
| `/a/showPanelMemberDashBoard.do` | 57 | 1702 |
| `/a/ajs/survey-angular.panel.analytics.reporting.v2.ajs.iron.PanelReportingAJSHandler-GetSurveyResponseStatusTrends` | 53 | 1 |
| `/a/ajs/survey-angular.panel.portal.PortalRewardAJSHandler-GetAllAvailableRewards` | 47 | 649 |
| `/a/ajs/survey-angular.panel.portal.DiscussionTopicAJSHandler-AddUpdateComment` | 44 | 14 |
| `/a/ajs/survey-angular.panel.portal.PortalDashBoardAJSHandler-GetSurveyDetails` | 35 | 1334 |
| `/a/ajs/survey-angular.panel.portal.PanelMemberAccountAJSHandler-GetPointsHistory` | 32 | 215 |
| `/a/ajs/survey-angular.panel.portal.PanelMemberAJSHandler-GetLoggedMemberDetails` | 30 | 2122 |
| `/a/ajs/survey-angular.panel.portal.PortalSurveyAJSHandler-GetAllSurveys` | 26 | 1951 |
| `/a/ajs/survey-angular.panel.portal.PanelMemberCustomFieldAJSHandler-GetPanelMemberCustomField` | 24 | 118 |
| `/a/showPanelProjectHistory.do` | 24 | 27 |
| `/a/ajs/survey-angular.panel.portal.DiscussionTopicAJSHandler-GetAllDiscussionTopicTags` | 23 | 19 |

---

## Copy-paste block

```
Top 20 Slowest Queries
         • /getSurveyAbandonedMembers – Latency : 8758 ms
         • /getCrosstabResults – Latency : 2409 ms
         • /reminderCount.do – Latency : 960 ms
         • /sendSurveyToFilteredMember – Latency : 653 ms
         • /showPanelAdminSettings.do – Latency : 640 ms
         • /showPanelProjectReminder.do – Latency : 406 ms
         • /getAtRiskMembers – Latency : 388 ms
         • /approveReward.do – Latency : 380 ms
         • /redeemReward – Latency : 323 ms
         • /showMembers.do – Latency : 306 ms
         • /api/nativehtml/panel.reward.PanelRewardRedeem – Latency : 294 ms
         • /getPanelFilter – Latency : 269 ms
         • /searchMember.do – Latency : 258 ms
         • /updateFilteredMemberStatus – Latency : 258 ms
         • /ShareCrosstab – Latency : 256 ms
         • /newPanelWizardName.do – Latency : 253 ms
         • /showRewardResolvedLog.do – Latency : 248 ms
         • /showRewardHistoryLog.do – Latency : 236 ms
         • /getActiveMembersTrend – Latency : 233 ms
         • /getEngagementTrends – Latency : 228 ms
```