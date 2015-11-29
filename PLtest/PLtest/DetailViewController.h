//
//  DetailViewController.h
//  PLtest
//
//  Created by 韩伟 on 15/11/10.
//  Copyright © 2015年 CLoud7. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface DetailViewController : UIViewController

@property (strong, nonatomic) id detailItem;
@property (weak, nonatomic) IBOutlet UILabel *detailDescriptionLabel;

@end

