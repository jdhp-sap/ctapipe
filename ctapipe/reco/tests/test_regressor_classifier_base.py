from ctapipe.reco.regressor_classifier_base import *

from sklearn.ensemble import RandomForestClassifier


def test_reshuffle_event_list():

    feature_list = [
            {"FlashCam": [[1, 10], [2, 20]],
             "ASTRICam": [[30, 3], [40, 4]]},
            {"FlashCam": [[1.5, 15]],
             "ASTRICam": [[35, 3.5], [25, 2.5], [30, 3]]}
    ]
    target_list = ["1", "2"]

    cam_id_list = ["FlashCam", "ASTRICam"]
    my_base = RegressorClassifierBase(model=RandomForestClassifier,
                                      cam_id_list=cam_id_list, unit=1)

    feature_flattened, target_flattened = my_base.reshuffle_event_list(feature_list,
                                                                       target_list)

    assert feature_flattened == {'FlashCam': [[1, 10], [2, 20], [1.5, 15]],
                                 'ASTRICam': [[30, 3], [40, 4], [35, 3.5], [25, 2.5],
                                              [30, 3]]}

    assert target_flattened == {'FlashCam': ['1', '1', '2'],
                                'ASTRICam': ['1', '1', '2', '2', '2']}
