# TODO: Fix Directory Paths in Plant Disease Detection System

## Information Gathered:
- Found 49 files containing old hardcoded directory paths
- Old pattern: `/home/amit/code_only/code/new/[disease_classifier]/csv|models|data/Test/Other_Images`
- New pattern: `/home/raju/code only/ds/plant_disease_detection_system/[disease_classifier]/csv|models|data/Test/Other_Images`

## Plan:
1. **Update all_data/src/** (2 files) ✅ DONE
   - all_data/src/top.py ✅
   - all_data/src/predict.py ✅

2. **Update apple_disease_classifier/src/** (2 files) ✅ DONE
   - apple_disease_classifier/src/top.py ✅
   - apple_disease_classifier/src/predict.py ✅

3. **Update bellpepper_disease_classifier/src/** (2 files) ✅ DONE
   - bellpepper_disease_classifier/src/top.py ✅
   - bellpepper_disease_classifier/src/predict.py ✅

4. **Update cherry_disease_classifier/src/** (2 files) ✅ DONE
   - cherry_disease_classifier/src/top.py ✅
   - cherry_disease_classifier/src/predict.py ✅

5. **Update corn(maize)_disease_classifier/src/** (2 files)
   - corn(maize)_disease_classifier/src/top.py
   - corn(maize)_disease_classifier/src/predict.py

6. **Update grape_disease_classifier/src/** (2 files)
   - grape_disease_classifier/src/top.py
   - grape_disease_classifier/src/predict.py

7. **Update peach_disease_classifier/src/** (2 files)
   - peach_disease_classifier/src/top.py
   - peach_disease_classifier/src/predict.py

8. **Update potato_disease_classifier/src/** (2 files)
   - potato_disease_classifier/src/top.py
   - potato_disease_classifier/src/predict.py

9. **Update strawberry_disease_classifier/src/** (2 files)
   - strawberry_disease_classifier/src/top.py
   - strawberry_disease_classifier/src/predict.py

10. **Update tomato_disease_classifier/src/** (2 files)
    - tomato_disease_classifier/src/top.py
    - tomato_disease_classifier/src/predict.py

## Update Pattern:
- Replace: `/home/amit/code_only/code/new/`
- With: `/home/raju/code only/ds/plant_disease_detection_system/`

## Follow-up Steps:
1. Verify all directory paths are updated correctly
2. Check that the new paths exist and are accessible
3. Test one or two files to ensure the changes work properly
