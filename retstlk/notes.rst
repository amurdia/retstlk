Anomalies check Requirements:
=============================
1. input: mls_id (list), start_date
2. check mapping for properties, classes and fields(list_date)
3. form query with list_date or modification_timestamp, standard_status and set expressions to get the count and sysid of active/pending listings.
4. get logs from prod logs ELK for these sysids from listing_lifecycle logs to see the breakage in the data flow.
5. if breakage is at downloader:
	1. check credentials.
	2. check download query.
	3. check sync query.
	4. check removed_statuses and statuses in lookup table.
6. if breakage is at normalizer:
	1. check metadata_id from metadata table and status of that metadata id in normalized_metadata table.
	2. if status is 15 , then check for handler errors (by running normalizer for these sysids in debug mode)
7. if breakage is at converter:
	1. check if sys_id is ignored, then check the attribute mapping.
8. send mail with detailed report on each module.

pace (complete data pipeline helper) requirements:
==================================================
1. Mapping:
	* one click metadata download
	* easy and detailed metadata view.
	* auto check with the previous metadata changes irrespective of whether it is present in staging.
	* mapping form for generating mappings.
	* NLP for automatically identifying the relatable fields for mapping.
	* first cut mapping report to be made available to user for human analysis.
	* auto download listing data based on config (default 1 week).
	* field-wise data showcase while mapping. Also display the variation in data for the same field. Smartly identify similar values like string of similar pattern of just string etc.
	* AI and ML to learn from the human changes.
	* Live enable/disable certain resources or classes for further process.
	* auto detect regularly changing fields to be excluded from hashing.
	* Live checkout fields from hashing with already provided auto detected fields.
	* Live attribute mapping based on the lookup values.
	* Generate, sync and store mapping report in a google sheet.
	* Image download with option to download via object, url or media resource along with corresponsing listing data for human analysis.
	* external plugs (these can change in format or functionality):
		* MLSCredentials.json to be updated based on details here.
		* MLS_<mls_id>.json to be updated based on mappings here.
		* generate.json to be updated based on excluded classes and resources.
		* modified downloader module for testing the Credential udpates.
		* modified normalizer module for testing the mappings.
		* modified converter module for testing the attribute mappings.
		* modified imagedownloader module for testing the images.
	* test suite:
		* Downloader test suite to check downloaded listings to be matching the set criteria and check the field/attribute mapped fields for any anomalies.
		* normalizer test suite to check if the normalized values are aligned with desired ones. If not, propose the special handlers.
		* converter test suite to check if attribute mapping is in sync and listings are not getting ignored due to that.
		* imagedownloader test suite to check the download reliability and time and propose any known modifications to improve the same.
	* test suites must be pluggable to work with any model whatsoever attached.
	* option to process all the modules for given set of listings, starting from downloader to imagedownloader.