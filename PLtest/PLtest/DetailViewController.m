//
//  DetailViewController.m
//  PLtest
//
//  Created by 韩伟 on 15/11/10.
//  Copyright © 2015年 CLoud7. All rights reserved.
//

#import "DetailViewController.h"
#import <PLCameraStreamingKit/PLCameraStreamingKit.h>

@interface DetailViewController ()

@end

@implementation DetailViewController

#pragma mark - Managing the detail item

- (void)setDetailItem:(id)newDetailItem {
    if (_detailItem != newDetailItem) {
        _detailItem = newDetailItem;
            
        // Update the view.
        [self configureView];
    }
}

- (void)configureView {
    // Update the user interface for the detail item.
    if (self.detailItem) {
        self.detailDescriptionLabel.text = [self.detailItem description];
    }
}

- (void)viewDidLoad {
    [super viewDidLoad];
    void (^permissionBlock)(void) = ^{ /* 下一步我们就添加这部分的代码 */};
    void (^noPermissionBlock)(void) = ^{ /* 处理未授权情况 */};
    
    // 检查摄像头是否有授权
    PLAuthorizationStatus status = [PLCameraStreamingSession cameraAuthorizationStatus];
    
    if (PLAuthorizationStatusNotDetermined == status) {
        [PLCameraStreamingSession requestCameraAccessWithCompletionHandler:^(BOOL granted) {
            // 回调确保在主线程，可以安全对 UI 做操作
            granted ? permissionBlock() : noPermissionBlock();
        }];
    } else if (PLAuthorizationStatusAuthorized == status) {
        permissionBlock();
    } else {
        noPermissionBlock();
    }
    [self configureView];
    
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

        
@end
