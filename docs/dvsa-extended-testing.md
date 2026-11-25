
# DVSA API – Extended Testing

## 1. Objective
Investigate the DVSA MOT History API's ability to retrieve historical MOT defects, advisories, failures and mileage records using vehicles with more extensive MOT histories.

## 2. Test Overview
- Authentication: Successful
- API response: HTTP 200
- Vehicle lookup: Successful
- Multiple historical MOT records: Retrieved
- Defect descriptions: Retrieved
- Defect classifications: Retrieved

## 3. Defect Data Structure

Each MOT test can contain a `defects` array.

Individual defect records contain:
- `dangerous`
- `text`
- `type`

## 4. Defect Classifications Identified

- ADVISORY
- MINOR
- MAJOR
- PRS
- USER ENTERED

## 5. Examples of Retrieved Defects

| Description | Classification |
|---|---|
| Tyre worn close to legal limit | ADVISORY |
| Tyre cracking or perishing | ADVISORY |
| Track rod end ball joint with slight play | ADVISORY |
| Slightly damaged wing mirror | MINOR |
| Fractured or broken coil spring | MAJOR |
| Windscreen washer not working | PRS |
| Headlamp not working | PRS |

## 6. Additional Historical Information

The API successfully retrieved:
- MOT test completion dates
- MOT expiry dates
- Recorded mileage
- Test results
- Historical defects and advisories

## 7. Data Limitations

- MOT defects represent inspection findings, not confirmed underlying mechanical diagnoses.
- Historical advisories do not establish whether an issue was subsequently repaired.
- Mileage readings are recorded at individual inspection dates.
- Empty defect arrays do not establish that a vehicle has no underlying mechanical faults.
- MOT records do not consistently provide verified repair outcomes.

## 8. Conclusion

Extended testing confirmed that the DVSA MOT History API can retrieve detailed historical inspection information, including advisories, minor and major defects, PRS records and historical MOT failures. This information can provide supporting evidence for vehicle profiling and preventative maintenance recommendations, subject to the limitations of MOT inspection data.
