create table if not exists avenue_gp.loan_performance (
reference_pool_id VARCHAR(100),
loan_identifier VARCHAR(100),
monthly_reporting_period VARCHAR(100),
channel_val VARCHAR(100),
seller_name VARCHAR(100),
servicer_name VARCHAR(100),
master_servicer VARCHAR(100),
original_interest_rate VARCHAR(100),
current_interest_rate VARCHAR(100),
original_upb VARCHAR(100),
upb_at_issuance VARCHAR(100),
current_actual_upb VARCHAR(100),
original_loan_term VARCHAR(100),
origination_date VARCHAR(100),
first_payment_date VARCHAR(100),
loan_age VARCHAR(100),
remaining_months_to_legal_maturity VARCHAR(100),
remaining_months_to_maturity VARCHAR(100),
maturity_date VARCHAR(100),
original_loan_to_value_ratio_ltv VARCHAR(100),
original_combined_loan_to_value_ratio_cltv VARCHAR(100),
number_of_borrowers VARCHAR(100),
debttoincome_dti VARCHAR(100),
borrower_credit_score_at_origination VARCHAR(100),
coborrower_credit_score_at_origination VARCHAR(100),
first_time_home_buyer_indicator VARCHAR(100),
loan_purpose VARCHAR(100),
property_type VARCHAR(100),
number_of_units VARCHAR(100),
occupancy_status VARCHAR(100),
property_state VARCHAR(100),
metropolitan_statistical_area_msa VARCHAR(100),
zip_code_short VARCHAR(100),
mortgage_insurance_percentage VARCHAR(100),
amortization_type VARCHAR(100),
prepayment_penalty_indicator VARCHAR(100),
interest_only_loan_indicator VARCHAR(100),
interest_only_first_principal_and_interest_payment_date VARCHAR(100),
months_to_amortization VARCHAR(100),
current_loan_delinquency_status VARCHAR(100),
loan_payment_history VARCHAR(100),
modification_flag VARCHAR(100),
mortgage_insurance_cancellation_indicator VARCHAR(100),
zero_balance_code VARCHAR(100),
zero_balance_effective_date VARCHAR(100),
upb_at_the_time_of_removal VARCHAR(100),
repurchase_date VARCHAR(100),
scheduled_principal_current VARCHAR(100),
total_principal_current VARCHAR(100),
unscheduled_principal_current VARCHAR(100),
last_paid_installment_date VARCHAR(100),
foreclosure_date VARCHAR(100),
disposition_date VARCHAR(100),
foreclosure_costs VARCHAR(100),
property_preservation_and_repair_costs VARCHAR(100),
asset_recovery_costs VARCHAR(100),
miscellaneous_holding_expenses_and_credits VARCHAR(100),
associated_taxes_for_holding_property VARCHAR(100),
net_sales_proceeds VARCHAR(100),
credit_enhancement_proceeds VARCHAR(100),
repurchase_make_whole_proceeds VARCHAR(100),
other_foreclosure_proceeds VARCHAR(100),
noninterest_bearing_upb VARCHAR(100),
principal_forgiveness_amount VARCHAR(100),
original_list_start_date VARCHAR(100),
original_list_price VARCHAR(100),
current_list_start_date VARCHAR(100),
current_list_price VARCHAR(100),
borrower_credit_score_at_issuance VARCHAR(100),
coborrower_credit_score_at_issuance VARCHAR(100),
borrower_credit_score_current VARCHAR(100),
coborrower_credit_score_current VARCHAR(100),
mortgage_insurance_type VARCHAR(100),
servicing_activity_indicator VARCHAR(100),
current_period_modification_loss_amount VARCHAR(100),
cumulative_modification_loss_amount VARCHAR(100),
current_period_credit_event_net_gain_or_loss VARCHAR(100),
cumulative_credit_event_net_gain_or_loss VARCHAR(100),
homeready_program_indicator VARCHAR(100),
foreclosure_principal_writeoff_amount VARCHAR(100),
relocation_mortgage_indicator VARCHAR(100),
zero_balance_code_change_date VARCHAR(100),
loan_holdback_indicator VARCHAR(100),
loan_holdback_effective_date VARCHAR(100),
delinquent_accrued_interest VARCHAR(100),
property_valuation_method VARCHAR(100),
high_balance_loan_indicator VARCHAR(100),
arm_initial_fixedrate_period___yr_indicator VARCHAR(100),
arm_product_type VARCHAR(100),
initial_fixedrate_period VARCHAR(100),
interest_rate_adjustment_frequency VARCHAR(100),
next_interest_rate_adjustment_date VARCHAR(100),
next_payment_change_date VARCHAR(100),
index_val VARCHAR(100),
arm_cap_structure VARCHAR(100),
initial_interest_rate_cap_up_percent VARCHAR(100),
periodic_interest_rate_cap_up_percent VARCHAR(100),
lifetime_interest_rate_cap_up_percent VARCHAR(100),
mortgage_margin VARCHAR(100),
arm_balloon_indicator VARCHAR(100),
arm_plan_number VARCHAR(100),
borrower_assistance_plan VARCHAR(100),
high_loan_to_value_hltv_refinance_option_indicator VARCHAR(100),
deal_name VARCHAR(100),
repurchase_make_whole_proceeds_flag VARCHAR(100),
alternative_delinquency_resolution VARCHAR(100),
alternative_delinquency_resolution_count VARCHAR(100),
total_deferral_amount VARCHAR(100),
created_by VARCHAR(100),
created_at timestamp, 
PRIMARY KEY (loan_identifier, monthly_reporting_period)
)